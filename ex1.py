print(f'Calcul d\'un prêt immobilier ou d\'un crédit à la consommation')
s = int(input('Entrez le montant du prêt ou crédit :'))
t = float(input('Entrez le taux annuel en %:'))
n = int(input('Entrez le nombre d\'années :'))

#tm = (1+t/100**(1/12)-1
tm = t/12/100
a = (1+tm)**(12*n)
m = s*tm*a/(a-1)
b = n*12

inte1 = s*tm
cr = tm - interet
print(f'La mensualité est de {tm} euros.')
print(f'La mensualité avec intérêts est de {round(m,2)} euros.')
print(f'Le montant des intérêts remboursés sont de {round(m*12n-s,2)} euros.')
#print(f'Le montant des intérêts remboursés sont de {a} euros.')
#print(f'Le taux mensuel est de {m} euros.')
print(f'Le taux mensuel est de {tm} euros.')
print('\nTableau d\'amortissement:')
#print(f'Tableau d\'amortissement:')
print('Mois - Mensualité - Intérêts - Capital remboursé - Capital restant - Intérêts remboursés')

#version du prof
ir=0
for i in (b):
    ir = 0
    i = s*tm
    cr = m-i
    crd=s-cr
    ir = i + ir

    print(f'{i+1} - {round(m,1)} - {round(i,1)} - {round(cr,1)} - {round(crd, 1)} - {round(ir,2)}')
    s=crd

"""
#version brouillon
for i in (b):
    interet = (s*1)*tm
    cr = tm - interet
    print(f'{i} - {tm} - {interet} - {} - Capital restant - Intérêts remboursés')

"""
