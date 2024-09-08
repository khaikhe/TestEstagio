def pertence_fibonacci(numero):

    fib_1, fib_2 = 0, 1
    
   
    if numero == 0 or numero == 1:
        return True
    
    
    while fib_2 < numero:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    
    
    return fib_2 == numero


numero_informado = int(input("Digite um numero: "))


if pertence_fibonacci(numero_informado):
    print(f"O número {numero_informado} é um numero Fibonacci.")
else:
    print(f"O número {numero_informado} não é Fibonacci.")
