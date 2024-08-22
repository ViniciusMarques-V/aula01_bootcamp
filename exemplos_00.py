#Calculando Bonus#

CONSTANTE_BONUS = 1000

nome = input("Digite o nome: ")
salario = input("Digite o pagode do cidadão: ")
perc_bonus = input("Digite o Bonus: ")

salario = float(salario)
perc_bonus = float(perc_bonus)

vlr_bonus =  salario * perc_bonus + CONSTANTE_BONUS

print(f"O usuario {nome} possui o bonus de {vlr_bonus}")
#print(vlr_bonus)
