# Versão 4: Organização em funções
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15

def obter_valor():
    try:
        v = float(input("Digite o valor: "))
        return v
    except ValueError:
        print("Entrada inválida. Insira um número.")
        return None

def obter_tipo():
    t = input("Tipo de conversão (CtoF/FtoC/CtoK/KtoC): ").strip().upper()
    if t not in ['CTOF','FTOC','CTOK','KTOC']:
        print("Tipo de conversão inválido")
        return None
    return t

def main():
    valor = obter_valor()
    if valor is None: return
    tipo = obter_tipo()
    if tipo is None: return

    conversoes = {
        'CTOF': (c_to_f, "°F"),
        'FTOC': (f_to_c, "°C"),
        'CTOK': (c_to_k, "K"),
        'KTOC': (k_to_c, "°C")
    }

    func, unidade = conversoes[tipo]
    resultado = func(valor)
    print(f"Resultado: {resultado}{unidade}")

if __name__ == "__main__":
    main()
