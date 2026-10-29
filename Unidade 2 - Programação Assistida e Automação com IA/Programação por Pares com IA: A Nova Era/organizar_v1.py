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
