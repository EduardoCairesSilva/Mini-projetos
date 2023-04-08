from time import sleep
from random import randint

formas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''\33[1;35m[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('')
jogador = int(input('Escolha uma opção: \33[m'))
print('\33[1;33mJO\33[m')
sleep(1)
print('\33[1;35mKEN\33[m')
sleep(1)
print('\33[1;36mPÔ\33[m')
sleep(2)
print('\33[1;31m-=-'*11)
print(f'Computador jogou {formas[computador]}')
print(f'Jogador jogou {formas[jogador]}')
print('-=-'*11)
print('\33[m')
# Possibilidades
if computador == 0:
    if jogador == 0:
        print('\33[1;31mEMPATE\33[m')
    elif jogador == 1:
        print('\33[1;34mJOGADOR VENCEU\33[m')
    elif jogador == 2:
        print('\33[1;34mCOMPUTADOR VENCEU\33[m')
    else:
        print('\33[1;31mJOGADA INVÁLIDA\33[m')

if computador == 1:
    if jogador == 0:
        print('\33[1;34mCOMPUTADOR VENCEU\33[m')
    elif jogador == 1:
        print('\33[1;31mEMPATE\33[m')
    elif jogador == 2:
        print('\33[1;34mJOGADOR VENCEU\33[m')
    else:
        print('\33[1;31mJOGADA INVÁLIDA\33[m')

if computador == 2:
    if jogador == 0:
        print('\33[1;34mJOGADOR VENCEU\33[m')
    elif jogador == 1:
        print('\33[1;34mCOMPUTADOR VENCEU\33[m')
    elif jogador == 2:
        print('\33[1;31mEMPATE\33[m')
    else:
        print('\33[1;31mJOGADA INVÁLIDA\33[m')
