# Programação Assistida e Automação com IA

## Identificação

- **Nome:** Kauã de Sousa e [NOME DO(A) COLEGA]
- **Turma:** [TURMA]
- **Data:** 29/10/2026
- **Ferramenta de IA utilizada:** Claude (Anthropic), via Claude Code
- **Problema escolhido:** Opção A — Organização de Arquivos

## 1. Problema

Pastas como `Downloads` acumulam arquivos de vários tipos misturados (PDFs, imagens, planilhas, textos). Organizar manualmente é **repetitivo, frequente, baseado em uma regra clara** (o tipo do arquivo) e **sujeito a erros** — por isso é uma boa candidata à automação.

Objetivo: criar um script Python que organize automaticamente os arquivos de uma pasta em **subpastas por extensão** (`pdf/`, `jpg/`, `txt/`...).

## 2. Entrada

- O caminho de uma pasta (informado na linha de comando; se omitido, a pasta atual).
- Os arquivos existentes dentro dessa pasta.

## 3. Processamento

1. Verificar se a pasta existe.
2. Listar apenas os **arquivos** da pasta (subpastas existentes são ignoradas).
3. Para cada arquivo, descobrir a extensão (em minúsculas: `.JPG` e `.jpg` vão para a mesma pasta).
4. Arquivos sem extensão vão para a subpasta `sem_extensao/`.
5. Criar a subpasta, se necessário, e mover o arquivo para ela.
6. Nunca sobrescrever um arquivo existente.

## 4. Saída esperada

- Arquivos movidos para subpastas com o nome da extensão.
- Mensagens no terminal mostrando cada movimentação (`foto.JPG -> jpg/`).
- Mensagem de erro clara em caso de problema (pasta inexistente, conflito de nomes).

Exemplo:

```
Antes:                    Depois:
downloads/                downloads/
├── Relatorio.pdf         ├── pdf/Relatorio.pdf
├── foto.JPG              ├── jpg/foto.JPG
├── notas.txt             ├── txt/notas.txt
├── dados.csv             ├── csv/dados.csv
└── README                └── sem_extensao/README
```

## 5. Prompt utilizado

```
PAPEL: Atue como desenvolvedor Python.

CONTEXTO: Sou estudante de Ciência da Computação e minha pasta de downloads
acumula arquivos de vários tipos misturados.

PROBLEMA: Quero organizar automaticamente os arquivos de uma pasta em
subpastas de acordo com a extensão de cada arquivo.

ENTRADA: o caminho de uma pasta, passado como argumento na linha de comando
(se não for informado, usar a pasta atual).

SAÍDA ESPERADA: cada arquivo movido para uma subpasta com o nome da sua
extensão em minúsculas (ex.: foto.JPG -> jpg/foto.JPG). Arquivos sem extensão
vão para "sem_extensao/". Mostrar no terminal cada arquivo movido.

LINGUAGEM: Python 3.

RESTRIÇÕES:
- usar somente a biblioteca padrão;
- não excluir nenhum arquivo;
- não mexer em subpastas já existentes;
- código simples, para um estudante iniciante entender.

CRITÉRIOS DE QUALIDADE: código legível, nomes de variáveis em português,
docstring explicando o objetivo.

CASOS DE TESTE:
1. pasta com arquivos .pdf, .JPG, .txt, .csv e um arquivo sem extensão;
2. pasta vazia;
3. pasta que não existe.

FORMATO: explique a estratégia, apresente o código e explique as
principais linhas.
```

## 6. Código inicial

Arquivo: [`organizar_v1.py`](organizar_v1.py)

```python
"""Versão inicial: organiza os arquivos de uma pasta em subpastas por extensão."""

import os
import shutil
import sys


def organizar(pasta):
    for nome in os.listdir(pasta):
        caminho = os.path.join(pasta, nome)
        if os.path.isfile(caminho):
            extensao = os.path.splitext(nome)[1][1:].lower()
            if extensao == "":
                extensao = "sem_extensao"
            destino = os.path.join(pasta, extensao)
            os.makedirs(destino, exist_ok=True)
            shutil.move(caminho, os.path.join(destino, nome))
            print(f"{nome} -> {extensao}/")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        organizar(sys.argv[1])
    else:
        organizar(".")
```

Explicação das principais linhas:

- `os.listdir(pasta)` lista tudo que há na pasta; `os.path.isfile` filtra só os arquivos.
- `os.path.splitext(nome)[1]` separa a extensão (`".JPG"`); `[1:]` remove o ponto e `.lower()` padroniza em minúsculas.
- `os.makedirs(destino, exist_ok=True)` cria a subpasta se ela ainda não existir.
- `shutil.move` move o arquivo para a subpasta.

## 7. Análise crítica

Checklist aplicado **antes** de executar:

| Pergunta | Resposta |
|---|---|
| Eu compreendo o código? | Sim — são poucas linhas e usa apenas `os`, `shutil` e `sys`. |
| O código atende ao problema definido? | Atende ao caso principal. |
| Há bibliotecas que eu não conheço? | Não; todas são da biblioteca padrão. |
| **Há operações que podem apagar ou sobrescrever dados?** | **Sim.** `shutil.move` pode **sobrescrever** um arquivo com o mesmo nome no destino. |
| O código utiliza dados sensíveis? | Não. |
| Há tratamento de erros? | **Não.** Qualquer erro interrompe o programa com um *traceback*. |
| Consigo explicar cada bloco? | Sim. |
| Existem casos que o código não considera? | Sim: pasta inexistente, conflito de nomes, um arquivo sem extensão com o mesmo nome de uma subpasta (ex.: arquivo `txt` e arquivo `a.txt`), e **não há como simular antes de mover**. |

Conclusão: a primeira versão funciona no caso normal, mas é **arriscada** para uso real, porque move arquivos imediatamente, sem simulação e sem proteção contra sobrescrita.

## 8. Casos de teste

Todos os testes foram executados de fato, em pastas de teste criadas para isso.

### Teste 1 — Caso normal

- **Entrada:** pasta com `Relatorio.pdf`, `foto.JPG`, `notas.txt`, `dados.csv`, `README` e a subpasta `antigos/`.
- **Esperado:** cada arquivo em sua subpasta; `antigos/` intacta; `README` em `sem_extensao/`.
- **Resultado (v1):** ✅ passou.

```
dados.csv -> csv/
foto.JPG -> jpg/
notas.txt -> txt/
README -> sem_extensao/
Relatorio.pdf -> pdf/
```

### Teste 2 — Caso limite: pasta vazia

- **Entrada:** pasta sem nenhum arquivo.
- **Esperado:** nada é alterado e o programa termina sem erro.
- **Resultado (v1):** ✅ passou, mas **não exibe nenhuma mensagem** — o usuário não sabe se o programa rodou.

### Teste 3 — Caso de erro: pasta inexistente

- **Entrada:** caminho `testes/nao_existe`.
- **Esperado:** mensagem de erro clara.
- **Resultado (v1):** ❌ o programa quebra com *traceback*:

```
FileNotFoundError: [WinError 3] O sistema não pode encontrar o caminho especificado: '.../nao_existe'
```

### Teste 4 — Conflito: arquivo com o mesmo nome já existe no destino

- **Entrada:** `pdf/relatorio.pdf` (conteúdo "ANTIGO") já existe, e um novo `relatorio.pdf` (conteúdo "NOVO") está na raiz.
- **Esperado:** nenhum arquivo perdido.
- **Resultado (v1):** ❌ **perda de dados.** O arquivo antigo foi sobrescrito sem nenhum aviso:

```
relatorio.pdf -> pdf/
./pdf/relatorio.pdf: NOVO      <- o conteúdo "ANTIGO" foi perdido
```

### Teste 5 — Arquivo sem extensão com nome igual a uma extensão

- **Entrada:** arquivos `a.txt` e `txt` (sem extensão) na mesma pasta.
- **Esperado:** organizar sem quebrar.
- **Resultado (v1):** ❌ o programa quebra ao tentar criar a pasta `txt/`, porque já existe um arquivo chamado `txt`:

```
FileExistsError: [WinError 183] Não é possível criar um arquivo já existente: '...\txt'
```

## 9. Problemas encontrados

1. **Sobrescrita silenciosa de arquivos (teste 4)** — o problema mais grave, porque causa perda de dados. O código "parecia certo" e passou no teste normal; só foi detectado com um teste específico.
2. **Sem tratamento de erros (testes 3 e 5)** — o usuário vê um *traceback* em vez de uma mensagem compreensível, e um único arquivo problemático interrompe a organização de todos os outros.
3. **Sem modo de simulação** — o script move os arquivos imediatamente, sem permitir conferir antes.
4. **Sem feedback na pasta vazia (teste 2)** e sem resumo ao final.

## 10. Prompt de refatoração

```
Revise o código abaixo. O programa já funciona no caso normal.

Nos meus testes encontrei estes problemas:
- quando já existe um arquivo com o mesmo nome no destino, ele é
  sobrescrito sem aviso (perda de dados);
- com uma pasta inexistente, o programa quebra com traceback;
- se existe um arquivo sem extensão chamado "txt" e um arquivo "a.txt",
  o programa quebra ao criar a pasta "txt";
- não há como simular antes de mover os arquivos.

Agora analise:
- clareza;
- organização;
- duplicação;
- nomes de variáveis e funções;
- tratamento de erros.

Sugira melhorias sem alterar o comportamento esperado (organizar por
extensão em minúsculas, "sem_extensao" para arquivos sem extensão,
não mexer em subpastas). Requisitos adicionais:
- nunca sobrescrever arquivos: renomear para nome_1.ext, nome_2.ext...;
- modo simulação como PADRÃO, e uma opção --executar para mover de verdade;
- um erro em um arquivo não deve interromper os demais;
- mostrar um resumo ao final.
Use somente a biblioteca padrão. Explique cada alteração proposta.

[CÓDIGO DA VERSÃO INICIAL]
```

## 11. Código refatorado

Arquivo: [`organizar_v2.py`](organizar_v2.py)

```python
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
```

Principais alterações e justificativas:

| Alteração | Justificativa |
|---|---|
| `destino_sem_conflito()` renomeia para `nome_1.ext` | Elimina a perda de dados do teste 4. |
| **Simulação por padrão** + `--executar` | O usuário confere o que vai acontecer antes de alterar qualquer arquivo. |
| Validação da pasta em `main()` | Mensagem clara em vez de *traceback* (teste 3). |
| `try/except OSError` por arquivo | Um arquivo problemático não interrompe os demais (teste 5). |
| Funções pequenas com nomes descritivos e docstrings | Cada função faz uma coisa só, o que facilita ler e testar. |
| `pathlib` em vez de `os.path` | Código mais legível (`pasta / nome`, `arquivo.suffix`). |
| `argparse` | Gera `--help` automaticamente e documenta as opções. |
| Constante `PASTA_SEM_EXTENSAO` | Evita "texto mágico" espalhado no código. |
| Resumo final e código de saída `1` em caso de erro | Feedback ao usuário e possibilidade de uso em outros scripts. |
| `sorted(...)` | Ordem previsível: a saída é sempre a mesma em qualquer sistema. |

### Resultados dos testes na versão refatorada

| Teste | Versão inicial | Versão refatorada |
|---|---|---|
| 1 — Caso normal | ✅ Organizou | ✅ Organizou (e na simulação **não** alterou nada) |
| 2 — Pasta vazia | ⚠️ Sem mensagem | ✅ "Nenhum arquivo para organizar." |
| 3 — Pasta inexistente | ❌ *Traceback* | ✅ "ERRO: a pasta '...' não existe ou não é uma pasta." |
| 4 — Conflito de nome | ❌ **Sobrescreveu o arquivo** | ✅ Salvou como `relatorio_1.pdf`; o original foi preservado |
| 5 — Arquivo `txt` + `a.txt` | ❌ *Traceback*, parou tudo | ✅ Reportou o erro em `a.txt`, continuou e moveu `txt` para `sem_extensao/`; ao rodar de novo, `a.txt` foi para `txt/` |

Saída do teste 4 na versão refatorada:

```
relatorio.pdf -> pdf/ (renomeado para relatorio_1.pdf)

Resumo: 1 movidos, 1 renomeados por conflito, 0 com erro.

./pdf/relatorio.pdf: ANTIGO
./pdf/relatorio_1.pdf: NOVO
```

## 12. Comparação

Notas de 1 a 5:

| Critério | Inicial | Refatorado |
|---|---:|---:|
| Funcionamento | 2 | 5 |
| Clareza | 4 | 4 |
| Organização | 2 | 5 |
| Legibilidade | 4 | 4 |
| Tratamento de erros | 1 | 5 |
| Facilidade de manutenção | 2 | 4 |

A versão inicial é **mais curta e fácil de ler à primeira vista**, por isso as notas de clareza e legibilidade ficaram próximas. A refatorada é mais longa, mas é **segura para uso real**: a versão inicial só funciona no caso ideal e pode apagar dados sem avisar.

## 13. Reflexão

> ✏️ *Rascunho — revisar e reescrever com as palavras da dupla.*

- **Onde a IA mais ajudou?** Na geração rápida da primeira versão e na refatoração: ela sugeriu `pathlib`, `argparse` e a função de renomear em caso de conflito, recursos que deixaram o código mais robusto.
- **Onde a IA errou?** A primeira versão não tratava conflitos de nome e podia **sobrescrever arquivos sem avisar**. O código parecia correto e passou no teste normal; o erro só apareceu quando criamos um teste específico para esse caso.
- **O que precisei modificar?** Exigir no prompt de refatoração: nunca sobrescrever arquivos, simulação como padrão, tratamento de erro por arquivo e mensagens claras. Também foi preciso pensar nos casos de teste 4 e 5, que a IA não tinha considerado no início.
- **Consigo explicar o código?** Sim. Cada função tem uma responsabilidade: `nome_da_subpasta` decide a pasta, `destino_sem_conflito` escolhe um nome livre, `organizar` percorre e move os arquivos, e `main` cuida dos argumentos e da validação.

### Respostas do Take Away da aula

1. **Em qual etapa a IA foi mais útil?** Na **refatoração**: ela transformou uma solução frágil em uma solução segura e organizada, explicando cada mudança.
2. **Qual parte exigiu mais raciocínio humano?** Definir **os casos de teste**, principalmente imaginar o conflito de nomes e o arquivo `txt` sem extensão. Foi isso que revelou os erros.
3. **A primeira solução funcionou?** Funcionou no caso normal, mas falhou em 3 dos 5 testes, e o teste 4 causou perda de dados.
4. **O que mudou após a refatoração?** Simulação por padrão, proteção contra sobrescrita, mensagens de erro claras, resumo final e código dividido em funções.
5. **Conseguiria explicar o programa sem consultar a IA?** Sim.
6. **Principal risco identificado?** Confiar em um código que "parece certo" e executá-lo direto na pasta real. Um script que move arquivos pode causar **perda de dados irreversível**.

## 14. Take Away

**"Programar com IA não significa deixar a IA programar por mim. Significa** usar a IA como uma parceira que acelera a escrita do código, enquanto eu continuo responsável por entender o problema, testar a solução, encontrar as falhas e decidir o que vai para produção."

### Cinco regras para usar IA de maneira responsável

1. **Planeje antes de pedir:** defina entrada, processamento, saída e restrições antes de escrever o prompt.
2. **Nunca execute sem entender:** se você não consegue explicar um trecho, não use esse trecho.
3. **Teste além do caso feliz:** sempre crie testes de caso limite e de erro, porque a IA costuma cobrir só o cenário ideal.
4. **Proteja os dados:** em scripts que alteram, movem ou apagam arquivos, use simulação e backup, e nunca coloque senhas, tokens ou dados pessoais no prompt.
5. **Assuma a responsabilidade:** a IA sugere, mas o código entregue é seu. Revise, valide e só depois faça o commit.
