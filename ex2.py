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

print('Calcul du capital acquis et de ses intérêts versé lorsque intérêts sont calculés une fois par an.')
p = int(input('Entrer le placement de départ :'))
m = int(input('Entrer le montant du versement mensuel :'))
t = int(input('Entrer le taux annuel :'))
n = int(input('Entrer le nombre d\'années :'))

for j in range ():


print(f'Le capital acquis avec intérêts est de {} euros au bout de {n} ans avec des versements mensuels de {m} euros.')
print(f'Les intérêts gagnés avec taux annuels de {t} % sont de {} euros.')
print(f'Sans placements avec intérêts, le capital acquis serait de {} euros.')
