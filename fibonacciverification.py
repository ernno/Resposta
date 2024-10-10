def verifica_numero():
    n = int(input("Digite o número a ser verificado como parte da sequência de Fibonacci: "))
    a = 0
    b = 1
    r = 10
    s = 0
    while r < 11:
        if s == n:
            print("O número faz parte da sequência de Fibonacci.")
            break
        elif s > n:
            print("O número não faz parte da sequência de Fibonacci.")
            break

        s = a+b
        a = b
        b = s

verifica_numero()