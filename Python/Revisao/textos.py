import time
nome= str(input('Digite o seu Nome: ')).strip() #vai eliminar os espaços presentes
print('Analisando seu nome...')
time.sleep(2)
print('seu nome em maiúsculas é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# Len () é uma função integrada ao Python que é utilizada para obter o número de itens em um determinado objeto, string, array, listas, entre outros 
#-nome.count(' ') isso ira contar a quantidade caracteres menos o espaço entre as letras 
#print(' seu primeiro nome tem {} letras '.format(nome.find(' '))) 
separa= nome.split() #split vai criar uma lista 
print(separa)