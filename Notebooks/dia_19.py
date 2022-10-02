#Exemplo identação
#def sacar(valor):
#   saldo = 500  
#    if saldo >= valor:
#       print('saque concluído')       
#sacar(100)

#if ternario
saldo = 500
saque = 100

status = "Sucesso" if saldo >= saque else "Falha"
print(f'{status} ao realizar saque')

#estruturas de repetição
texto = input('Informe um texto')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print (letra, end='')
        
print() #adiciona uma quebra de linha
