import math
num = int(input('digite um número:'))
raiz=math.sqrt(num)
print('a raiz de {} é igual a {:.2f}'.format(num, math.ceil(raiz)))
# math.ceil(raiz) arredonda o valor da raiz para cima  e math.floor(raiz)-> arredonda para alto 