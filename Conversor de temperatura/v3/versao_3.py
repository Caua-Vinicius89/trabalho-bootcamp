# Versão 3: Validação de entrada
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15

def main():
    try:
        valor = float(input("Digite o valor: "))
    except ValueError:
        print("Entrada inválida. Insira um número.")
        return

    tipo = input("Tipo de conversão (CtoF/FtoC/CtoK/KtoC): ").strip().upper()
    conversoes = {
        'CTOF': (c_to_f, "°F"),
        'FTOC': (f_to_c, "°C"),
        'CTOK': (c_to_k, "K"),
        'KTOC': (k_to_c, "°C")
    }

    if tipo not in conversoes:
        print("Tipo de conversão inválido")
        return

    func, unidade = conversoes[tipo]
    resultado = func(valor)
    print(f"Resultado: {resultado}{unidade}")

if __name__ == "__main__":
    main()
