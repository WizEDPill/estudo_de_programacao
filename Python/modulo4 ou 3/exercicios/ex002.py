'''crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
depois disso mostre a listagem de numeros gerádos e tambem indique o menor e maior 
que estão na tupla '''

from random import randint
lista= (randint(1,100), randint(1,100), randint(1,100), randint(1,100))#int de inteiro
print(lista)
print(max(int(number) for number in lista))# puxando maximo numero inteiro gerado dentro da lista 
print(min(int(number)for number in lista))# puxando o menor numero na lista da lista 
# outra forma é : 
print(f'o maior numero sorteador foi {max(lista)}')
print(f'o menor valor sorteado foi {min(lista)}')