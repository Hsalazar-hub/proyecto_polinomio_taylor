#!/usr/bin/env python3
"""
Proyecto Polinomio de Taylor.
Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


def derivada(f, h = 0.01):
    """
    Retorna la función derivada de f dado un h.
    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _


def polinomio_taylor(f, x0, n):
    """
    Implementa y retorna el Polinomio de Taylor de grado n centrado en x0.
    Parámetros:
    f: función de variable real f(x).
    x0: punto centro del polinomio.
    n: grado del polinomio.
    """
    
    
    def polit(x):
        i=0
        dervX = f 
        C=0  
        while(i<n):
            if C != 0:
                C += ((dervX(x0))/(math.factorial(i)))*((x-x0)**(i))
                dervX = derivada(dervX)
            else:
                C= dervX(x0)
            i= i+1
            return C

    return polit

if __name__ == '__main__':
   e= lambda P,Q : math.fabs((P-Q)/P)
   r= lambda x : math.log(x)
   pt= polinomio_taylor(r,3,6)

   V = 1.1

   print('valor aproximado', pt(V))