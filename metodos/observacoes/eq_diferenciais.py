from sympy import Function, dsolve, Eq

f = Function('f')

#Definido a equação diferencial
eq_dif = Eq(f(x) - diff(f(x), x), 0)
print(eq_dif)

print(dsolve(eq_dif, f(x)))