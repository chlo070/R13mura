#type assurance vie
""" aide
m : mensualité
t : taux
n : nb d'années
1e année : [(m*12)*(1+t/100)] = c(n)
2e année : {(m*12) + [<1e année>]} * (1+t/100)

c : capital acquis
ci : capital acquis avec intérêts
csi : capital acquis sans intérêts
"""
"""
#exercice 1
print('Calcul du capital acquis et de ses intérêts versés lorsque intérêts sont calculés une fois par an.')
p = int(input('Entrer le placement de départ :'))
m = int(input('Entrer le montant du versement mensuel :'))
t = float(input('Entrer le taux annuel en % :'))
n = int(input('Entrer le nombre d\'années :'))

c = p
i = 0
for j in range (n):
    c = ((m*12) + c) * (1+t/100)
    i = c - p
    csi = ((m*12) + c) - p
print(f'Le capital acquis avec intérêts est de {round(c,2)} euros au bout de {n} ans avec des versements mensuels de {m} euros.')
print(f'Les intérêts gagnés avec taux annuels de {t} % sont de {round(i,2)} euros.')
print(f'Sans placements avec intérêts, le capital acquis serait de {round(csi,2)} euros.')

"""
#exercice 2
print('Calcul du capital acquis et de ses intérêts versés lorsque intérêts sont calculés une fois par mois.')
p = int(input('Entrer le placement de départ :'))
m = int(input('Entrer le montant du versement mensuel :'))
t = float(input('Entrer le taux annuel en % :'))
n = int(input('Entrer le nombre d\'années :'))


c = p
i = 0
for j in range (n*12):
    c = (m + c) * (1+t/(12*100))
    i = c - p
    csi = (m + c) - p
print(f'Le capital acquis avec intérêts est de {round(c,2)} euros au bout de {n} ans avec des versements mensuels de {m} euros.')
print(f'Les intérêts gagnés avec taux annuels de {t} % sont de {round(i,2)} euros.')
print(f'Sans placements avec intérêts, le capital acquis serait de {round(csi,2)} euros.')

