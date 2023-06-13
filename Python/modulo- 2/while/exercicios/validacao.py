sexo= str(input('Informe seu sexo [M/F]')).strip().upper()[0]# DESSE UPER VOU TIRAR AS ´RIMEIRAS LETRAS

while sexo not in 'MmFf':# enquanto o sexo não estive em masculino ou feminino
    sexo= str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
    
print('Sexo{}registrado com sucesso'.format(sexo))


