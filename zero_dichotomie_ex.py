import math 

"""
PROMPT: 
Ecrire une fct zero_dichotomie(f,a,b,eps) qui prend en argument une fct f, les bornes a et b d'un intervalle et la précision eps, 
et qui renvoie la solution approchée de l'équation f(x) = 0 sur [a,b] à eps près.
Exécuter le programme afin d 'obtenir la solution à 10
"""

def zero_dichotomie(f, a, b, eps):
    signe = f(a)
    while b-a > eps:
        m = (a+b)/2
        if signe + f(m) < eps:
            b = m
        else: 
            a = m
    return (a+b)/2

def f(x):
    return math.log(x) - 2 * x

print(zero_dichotomie(f, 1, 2, 0.001))