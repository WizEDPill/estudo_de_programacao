print('Programa de Fibonacci')
n1= int(input('quantos valores serão operados ?'))
print('-=-'*20)
t1=0
t2=1 
print('{} -> {}'.format(t1,t2))
numb= 3
while numb <= n1: 
    t3= t1+t2 
    print('->{}'.format(t3))
    t1=t2 
    t2=t3 
    numb+=1 
    print('->Fom')
 