print("""[1] = Sem porcentagem
[2] = Com porcentagem""")

escolha = int(input("Escolha qual o tipo de calculadora quer usar: "))
if escolha == 1:
    a = int(input("Qual é o valor de A?: "))
    b = int(input("Qual é o valor de B?: "))
    So = a + b
    Su = a - b
    Di = a / b
    Mu = a * b
    Po = a ** b
    print("""ESCOLHA QUAL OPERAÇÃO QUER OLHAR:
    [1] = Soma
    [2] = Subtração
    [3] = Divisão
    [4] = Multiplicação
    [5] = Potência""")
    escolha2 = int(input("Escolha qual operação deseja realizar: "))
    if escolha2 == 1:
        print(f"A soma será: {So}")
    elif escolha2 == 2:
        print(f"A sua subtração será: {Su}")
    elif escolha2 == 3:
        print(f"A sua divisão será: {Di}")
    elif escolha2 == 4:
        print(f"A sua multiplicação será: {Mu}")
    elif escolha2 == 5:
        print(f"A sua potência será: {Po}")
elif escolha == 2:
    a = int(input("Qual é o valor de A?: "))
    b = int(input("Qual é o valor de B?: "))
    c = float(input("Qual será a porcentagem?: "))
    So = a + b
    Su = a - b
    Di = a / b
    Mu = a * b
    Pot = a ** b
    Por = a - b * c
    print("""ESCOLHA QUAL OPERAÇÃO QUER OLHAR:
    [1] = Soma
    [2] = Subtração
    [3] = Divisão
    [4] = Divisão
    [5] = Potência
    [6] = Porcentagem""")
    escolha2 = int(input("Escolha qual operação deseja realizar: "))
    if escolha2 == 1:
        print(f"A soma será: {So}")
    elif escolha2 == 2:
        print(f"A sua subtração será: {Su}")
    elif escolha2 == 3:
        print(f"A sua divisão será: {Di}")
    elif escolha2 == 4:
        print(f"A sua multiplicação será: {Mu}")
    elif escolha2 == 5:
        print(f"A sua potência será: {Pot}")
    elif escolha2 == 6:
        print(f"A sua porcentagem será: {Por}")
