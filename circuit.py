# Simulador simples de circuito elétrico (Valdeci)
# Baseado na Lei de Ohm: V = R * I

def calcular_corrente(tensao, resistencia):
    return tensao / resistencia

def calcular_tensao(corrente, resistencia):
    return corrente * resistencia

def calcular_resistencia(tensao, corrente):
    return tensao / corrente

def calcular_potencia(tensao, corrente):
    return tensao * corrente

def main():
    print("=== Simulador de Circuito Elétrico ===")
    
    print("\nEscolha o que deseja calcular:")
    print("1 - Corrente (I)")
    print("2 - Tensão (V)")
    print("3 - Resistência (R)")
    print("4 - Potência (P)")
    
    opcao = int(input("Opção: "))
    
    if opcao == 1:
        V = float(input("Digite a tensão (Volts): "))
        R = float(input("Digite a resistência (Ohms): "))
        I = calcular_corrente(V, R)
        print(f"Corrente: {I:.2f} A")
    
    elif opcao == 2:
        I = float(input("Digite a corrente (Ampères): "))
        R = float(input("Digite a resistência (Ohms): "))
        V = calcular_tensao(I, R)
        print(f"Tensão: {V:.2f} V")
    
    elif opcao == 3:
        V = float(input("Digite a tensão (Volts): "))
        I = float(input("Digite a corrente (Ampères): "))
        R = calcular_resistencia(V, I)
        print(f"Resistência: {R:.2f} Ω")
    
    elif opcao == 4:
        V = float(input("Digite a tensão (Volts): "))
        I = float(input("Digite a corrente (Ampères): "))
        P = calcular_potencia(V, I)
        print(f"Potência: {P:.2f} W")
    
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()