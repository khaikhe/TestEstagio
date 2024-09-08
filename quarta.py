
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def calcular_percentuais(faturamento):
    total = sum(faturamento.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentuais

def main():
    percentuais = calcular_percentuais(faturamento)

    estado_input = input("Digite a UF Desejada: SP, RJ, MG, ES, Outros): ").strip().upper()

    
    if estado_input in percentuais:
        print(f"Percentual {estado_input}: {percentuais[estado_input]:.2f}%")
    else:
        print("Estado inválido ou não existe.")

if __name__ == "__main__":
    main()
