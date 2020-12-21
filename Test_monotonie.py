import math

"""
PROMPT:
Ecrire une fct monotone(f,a,b,n) qui prend en argument une fct f, les bornes a et b d'un intervalle et le nombre
n de valeurs calculées, et afficheh suivant les cas le message "la fct n'est pas mnonotone" ou le message 
"la fct semble monotone".
Tester le programme avec la fct f définie sur l'intervalle [0,pi] par f(x) = x + 1.0001 cos(x)
Choisir  n  = 100 puis n = 1000
"""

def is_monotone(f,a,b,n):
    sens = f(b) - f(a)
    x = a
    dx = (b - a)/n
    test = True

    for k in range(n):
        if ((f(x+dx)-f(x))*sens) <0 : 
            print("la fct n'est pas monotone")
            print(x,x+dx)
            test = False
            break
        x +=dx
    if test == True:
        print("la fct semble monotone")

def f(x):
    return x+1.0001 * math.cos(x)

#Test
a = 0
b = math.pi

is_monotone(f, a,b,100)
print('\n')
is_monotone(f,a,b,1000)