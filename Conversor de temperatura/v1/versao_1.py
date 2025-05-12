# Versão 1: Esqueleto básico
def c_to_f(celsius):
    return (celsius * 9/5) + 32

def main():
    c = float(input("Digite a temperatura em Celsius: "))
    f = c_to_f(c)
    print(f"{c}°C equivalem a {f}°F")

if __name__ == "__main__":
    main()
