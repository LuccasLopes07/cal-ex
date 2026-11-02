"""Calculadora simples de terminal em Python."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def potencia(a, b):
    return a ** b


def resto(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível calcular o resto com divisor zero.")
    return a % b


OPERACOES = {
    "+": ("Soma", somar),
    "-": ("Subtração", subtrair),
    "*": ("Multiplicação", multiplicar),
    "/": ("Divisão", dividir),
    "**": ("Potência", potencia),
    "%": ("Resto da divisão", resto),
}


def ler_numero(mensagem):
    """Pede um número ao usuário até que um valor válido seja digitado."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 3 ou 2,5).")


def formatar(resultado):
    """Mostra números inteiros sem casas decimais desnecessárias."""
    if resultado == int(resultado):
        return str(int(resultado))
    return f"{resultado:.10g}"


def mostrar_menu():
    print("\n=== CALCULADORA ===")
    for simbolo, (nome, _) in OPERACOES.items():
        print(f"  {simbolo:<3} {nome}")
    print("  q   Sair")


def main():
    while True:
        mostrar_menu()
        escolha = input("\nEscolha a operação: ").strip().lower()

        if escolha == "q":
            print("Até logo!")
            break

        if escolha not in OPERACOES:
            print("Operação inválida. Tente novamente.")
            continue

        a = ler_numero("Primeiro número: ")
        b = ler_numero("Segundo número: ")

        nome, funcao = OPERACOES[escolha]
        try:
            resultado = funcao(a, b)
            print(f"\n{formatar(a)} {escolha} {formatar(b)} = {formatar(resultado)}")
        except ZeroDivisionError as erro:
            print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()