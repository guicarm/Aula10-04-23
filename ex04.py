# DADO UM NÚMERO E UM MÚLTIPLO, EXIBIR O PRÓXIMO MÚLTIPLO A PARTIR DO NÚMERO


# Digitar um número:
n = int(input("Digite um número: "))

# Digitar um múltiplo:
m = int(input("Digite um múltiplo: "))

n = n + 1
while n % m != 0:
    n = n + 1
print('Próximo múltiplo: ', n)
