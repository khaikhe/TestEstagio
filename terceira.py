import json

def calcular_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)

    valores = [item['valor'] for item in dados if item['valor'] > 0]
    
    if not valores:
        return None, None, 0

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)

    dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media


menor, maior, dias_acima_media = calcular_faturamento('faturamento.json')

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
