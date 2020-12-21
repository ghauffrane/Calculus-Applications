import math 

"""
PROMPT:
Déterminer unen valuer approchée du maximum de la fct f définie par f(x) = x * exp(-x)
sur l 'intervalle [0,2] en utilisant un algorithme déterministe à pas constant. Pour cela, écrire une fct 
maximum1(f, a, b, n) qui prend en argument une fct f, les bornes a et b d'un intervalle et le nombre n de valeurs
calculées, et renvoie une valeur approchée du maximum. Utiliser 1000 valeurs équiréparties sur [a,b] pour le test.
"""

def maximum1(f, a, b, n): 
    dx = (b-a)/n
    x = a
    maxi = f(x)

    for k in range(n):
        x += dx
        y = f(x)
        if y>maxi: 
            maxi = y
    return maxi

def f(x): 
    return x*math.exp(-x)

#Test
a = 0
b = 2
n = 1000

print('Maximum de f sur [a,b]:', maximum1(f,a,b,n))