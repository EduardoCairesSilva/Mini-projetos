def LeiaInt(msg):
    try:
        n = int(input(msg))
    except(ValueError, TypeError):
        print('DIGITE UM NÚMERO INTEIRO.')
    except KeyboardInterrupt:
        print('O usúario preferiu não continuar.')
    else:
        return n


def linha(tam=40):
    return '-' * tam


def titulo(txt):
    print(linha())
    print(txt)
    print(linha())


def menu(lista):
    titulo('SISTEMA V2')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opc = LeiaInt('Digite um valor: ')
    return opc


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except FileNotFoundError:
        print('Não foi possivel criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('ERROR. NÃO FOI POSSIVEL LER O ARQUIVO.')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:<3}')
    finally:
        a.close()


def cadastro(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except FileNotFoundError:
        print('NÃO FOI POSSIVEL ABRIRO ARQUIVO.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except FileNotFoundError:
            print('ERROR')
        else:
            a.close()


arq = 'SISTEMAV2.TXT'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resp = menu(['Pessoas cadastradas', 'Cadastrar nova pessoa', 'SAIR'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        titulo('CADASTRO DE PESSOA')
        nome = str(input('NOME: '))
        idade = LeiaInt('IDADE: ')
        cadastro(arq, nome, idade)
    elif resp == 3:
        print('PROGRAMA FINALIZADO.')
        break
    else:
        print('ERROR')
