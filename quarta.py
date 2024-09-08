# Dados do faturamento por estado
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
    # Calcular percentuais
    percentuais = calcular_percentuais(faturamento)

    # Solicitar ao usuário o estado desejado
    estado_input = input("Digite o estado que deseja ver o percentual (ex.: SP, RJ, MG, ES, Outros): ").strip().upper()

    # Exibir resultado
    if estado_input in percentuais:
        print(f"Percentual de representação de {estado_input}: {percentuais[estado_input]:.2f}%")
    else:
        print("Estado inválido ou não encontrado.")

if __name__ == "__main__":
    main()
