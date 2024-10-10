def verifica_string():
    s = input()
    contagem = 0
    for i in range(len(s)):
        if s[i] == "a":
            contagem += 1
        if s[i] == "A":
            contagem += 1
    if contagem == 0:
        print("O string digitado não possui a letra a.")
    else:
        print("O string digitado possui", contagem ,"letras a.")

verifica_string()