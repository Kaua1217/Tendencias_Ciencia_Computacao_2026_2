"""Organiza os arquivos de uma pasta em subpastas por extensão.

Por padrão roda em modo de simulação (apenas mostra o que faria).
Use --executar para mover os arquivos de verdade.

Exemplos:
    python organizar_v2.py C:/Users/aluno/Downloads
    python organizar_v2.py C:/Users/aluno/Downloads --executar
"""

import argparse
import shutil
import sys
from pathlib import Path

PASTA_SEM_EXTENSAO = "sem_extensao"


def nome_da_subpasta(arquivo: Path) -> str:
    """Retorna o nome da subpasta de destino com base na extensão do arquivo."""
    extensao = arquivo.suffix.lower().lstrip(".")
    return extensao or PASTA_SEM_EXTENSAO


def destino_sem_conflito(destino: Path) -> Path:
    """Se o destino já existir, gera um nome livre: arquivo_1.pdf, arquivo_2.pdf..."""
    if not destino.exists():
        return destino
    contador = 1
    while True:
        candidato = destino.with_name(f"{destino.stem}_{contador}{destino.suffix}")
        if not candidato.exists():
            return candidato
        contador += 1


def organizar(pasta: Path, executar: bool = False) -> dict:
    """Move cada arquivo da pasta para uma subpasta com o nome da sua extensão.

    Retorna um resumo com a quantidade de arquivos movidos, renomeados e com erro.
    Subpastas já existentes não são alteradas.
    """
    resumo = {"movidos": 0, "renomeados": 0, "erros": 0}
    arquivos = sorted(item for item in pasta.iterdir() if item.is_file())

    if not arquivos:
        print("Nenhum arquivo para organizar.")
        return resumo

    for arquivo in arquivos:
        subpasta = pasta / nome_da_subpasta(arquivo)
        try:
            if subpasta.exists() and not subpasta.is_dir():
                raise FileExistsError(f"já existe um arquivo chamado '{subpasta.name}'")

            destino = destino_sem_conflito(subpasta / arquivo.name)
            renomeado = destino.name != arquivo.name
            aviso = f" (renomeado para {destino.name})" if renomeado else ""
            print(f"{arquivo.name} -> {subpasta.name}/{aviso}")

            if executar:
                subpasta.mkdir(exist_ok=True)
                shutil.move(str(arquivo), str(destino))
            resumo["movidos"] += 1
            resumo["renomeados"] += renomeado
        except OSError as erro:
            print(f"ERRO ao mover {arquivo.name}: {erro}", file=sys.stderr)
            resumo["erros"] += 1

    return resumo


def main() -> int:
    parser = argparse.ArgumentParser(description="Organiza arquivos em subpastas por extensão.")
    parser.add_argument("pasta", nargs="?", default=".", help="pasta a organizar (padrão: pasta atual)")
    parser.add_argument("--executar", action="store_true",
                        help="move os arquivos de verdade (sem esta opção, apenas simula)")
    args = parser.parse_args()

    pasta = Path(args.pasta)
    if not pasta.is_dir():
        print(f"ERRO: a pasta '{pasta}' não existe ou não é uma pasta.", file=sys.stderr)
        return 1

    if not args.executar:
        print("MODO SIMULAÇÃO: nenhum arquivo será movido. Use --executar para aplicar.\n")

    resumo = organizar(pasta, args.executar)
    verbo = "movidos" if args.executar else "a mover"
    print(f"\nResumo: {resumo['movidos']} {verbo}, "
          f"{resumo['renomeados']} renomeados por conflito, {resumo['erros']} com erro.")
    return 1 if resumo["erros"] else 0


if __name__ == "__main__":
    sys.exit(main())
