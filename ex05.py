# DADO UM NÚMERO, EXIBIR SEU FATORIAL

# 1) PEGAR UM NÚMERO (não repetitivo)
# 2) DESCOBRIR O FATORIAL (repetitivo)
# 3) EXIBIR O FATORIAL (não repetitivo)

# 1) PEGAR UM NÚMERO (não repetitivo)
n = int(input("Digite um número: "))


# 2) DESCOBRIR O FATORIAL (repetitivo)
fatorial = 1
for volta in range(1, n + 1, 1):
   fatorial = fatorial *  volta


# 3) EXIBIR O FATORIAL (não repetitivo)
print("Fatorial = ", fatorial)