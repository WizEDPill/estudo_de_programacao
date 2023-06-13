soma= 0 # soma parte do 0 (contagem) 
cont=0
for c in range (1,501,2):
    if c % 3==0:
        cont=cont +1           # somador
        soma= soma + c # acumulador
print(' a soma de todos os {} valores solicitados  é  {} : '.format(cont,soma))