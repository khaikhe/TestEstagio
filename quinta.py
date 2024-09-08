def inverter_string(s):
   
    lista = list(s)
    
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
   
    return ''.join(lista)

def main():
   
    string_input = input("Digite uma string: ").strip()
    string_invertida = inverter_string(string_input)
    print(f"Inverção: {string_invertida}")

if __name__ == "__main__":
    main()
