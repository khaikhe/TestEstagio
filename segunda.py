def pertence_fibonacci(numero):
    # Iniciando a sequência de Fibonacci com 0 e 1
    fib_1, fib_2 = 0, 1
    
    # Verificar se o número é 0 ou 1, que são parte da sequência
    if numero == 0 or numero == 1:
        return True
    
    # Gerar os próximos números da sequência até que o valor ultrapasse o número dado
    while fib_2 < numero:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    
    # Se o número for igual a algum número gerado na sequência, ele pertence à sequência
    return fib_2 == numero

# Solicita ao usuário que informe o número
numero_informado = int(input("Digite um numero: "))

# Verifica se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero_informado):
    print(f"O número {numero_informado} é um numero Fibonacci.")
else:
    print(f"O número {numero_informado} não é Fibonacci.")
