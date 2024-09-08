import json

def carregar_dados(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    return dados

def main():
    dados = carregar_dados('faturamento.json')
    
    
    try:
        dia_input = int(input("Digite o número do dia: ").strip())
        
        if 1 <= dia_input <= 31:
            
            dia_dados = [item for item in dados if item['dia'] == dia_input]
            
            if dia_dados:
                print(f"Faturamento no dia {dia_input}: R${dia_dados[0]['valor']:.2f}")
            else:
                print("Dia não encontrado.")
        else:
            print("Número do dia inválido. Digite um número entre 1 e 31.")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()
