import math

"""
PROMPT:
Ecrire un programme permettant de calculer une valeur approchée de l'intégrale de x*exp(-x)dx entre 0 et 1 en utilisant
la méthode de trapèzes.
"""

def trapezes(f, a, b, n): 
    s = 0
    h = (b-a)/n
    x = a
    for i in range(n):
        xh = x+h
        s += h * (f(x) + f (xh))/2
        x = xh
        return s

def f(x):
    return x*math.exp(-x)

a = 0
b = 1
n = 1000
print(trapezes(f,a,b,n))