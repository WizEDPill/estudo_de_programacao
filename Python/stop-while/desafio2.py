sub=nu=0 
print('---'*10)
nu= int(input('informe que tabuada gostaria : '))
print('---'*10)
while True: 
     if sub>=10: 
        break
     sub+=1
     number=nu*(sub)
     print(f'o valor de {nu}x{sub} = {number}')
print('---'*10)
