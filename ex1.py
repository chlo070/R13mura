print(f'Calcul d\'un prêt immobilier ou d\'un crédit à la consommation')
p = int(input('Entrez le montant du prêt ou crédit :'))
t = int(input('Entrez le taux annuel :'))
n = int(input('Entrez le nombre d\'années :'))

tm = t/12/100
a = (1+tm)**(12*n)
m = p*tm*a/(a-1)
b = n*12

print(f'La mensualité est de {tm} euros.')
print(f'Le montant des intérêts remboursés sont de {a} euros.')
print(f'Le taux mensuel est de {m} euros.')

print(f'Tableau d\'amortissement:')
print('Mois - Mensualité - Intérêts - Capital remboursé - Capital restant - Intérêts remboursés')
for i in (b):
    print(f'{1} - {tm} - {p*tm} - Capital remboursé - Capital restant - Intérêts remboursés')

