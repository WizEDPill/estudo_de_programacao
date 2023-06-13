import random 
tentativas= 1
n1= int(input('acabei de pensar em um numero entre 0 e 10 tente advinhar e me fale: '))
numero= random.randint(0,10)
while n1!= numero:  
    n1= int(input('um numero entre 0 e 10 tente advinhar e me fale: '))
    tentativas+=1
print('finalmente voce acertor depois de {} tenativas'.format(tentativas))

