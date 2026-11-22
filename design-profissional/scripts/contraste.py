"""Calcule contraste de cores sólidas sRGB conforme WCAG 2.2."""
import argparse
import re


def luminancia(cor):
    valor = cor.removeprefix("#")
    if not re.fullmatch(r"(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", valor):
        raise argparse.ArgumentTypeError("use uma cor hexadecimal RGB, como #123 ou #123456")
    if len(valor) == 3:
        valor = "".join(canal * 2 for canal in valor)

    def linearizar(canal):
        if canal <= 0.04045:
            return canal / 12.92
        return ((canal + 0.055) / 1.055) ** 2.4

    vermelho, verde, azul = (
        linearizar(int(valor[indice:indice + 2], 16) / 255)
        for indice in (0, 2, 4)
    )
    return 0.2126 * vermelho + 0.7152 * verde + 0.0722 * azul


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primeira_cor", type=luminancia)
    parser.add_argument("segunda_cor", type=luminancia)
    args = parser.parse_args()

    escura, clara = sorted((args.primeira_cor, args.segunda_cor))
    razao = (clara + 0.05) / (escura + 0.05)
    print(f"Razão de contraste: {razao:.3f}:1")
    for limite in (3, 4.5):
        resultado = "atingido" if razao >= limite else "abaixo do limite"
        print(f"Limiar {limite:g}:1: {resultado}")


if __name__ == "__main__":
    main()
