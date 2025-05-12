# Versão 2: Suporte para múltiplas conversões
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15

def main():
    valor = float(input("Digite o valor: "))
    tipo = input("Tipo de conversão (CtoF/FtoC/CtoK/KtoC): ").strip().upper()
    if tipo == 'CTOF':
        resultado = c_to_f(valor); unidade="°F"
    elif tipo == 'FTOC':
        resultado = f_to_c(valor); unidade="°C"
    elif tipo == 'CTOK':
        resultado = c_to_k(valor); unidade="K"
    elif tipo == 'KTOC':
        resultado = k_to_c(valor); unidade="°C"
    else:
        print("Tipo de conversão inválido")
        return
    print(f"Resultado: {resultado}{unidade}")

if __name__ == "__main__":
    main()
