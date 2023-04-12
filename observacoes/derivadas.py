from sympy import diff, Symbol, sin, cos, exp, S

#Configuração
x = Symbol('x')
f = x**3
print(diff(f, x))

# Para derivadas de ordem superior
print(diff(f, x, 2))

#Derivadas Trigonométricas
print(diff(x**2 * sin(x), x))

f = S('1/2')*x**2
print(f)

df = diff(f, x)
print(df)