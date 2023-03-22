#recebe a função f, o extremo esquerdo (a), o extremo direito (b) e um erro 
def bisseccao (f, a, b, err, lim):
    fa = f(a)
    i = 0
    # O limitador é um aspecto computacional, para evitar loops eternos ou muito longos
    while (i < lim):
        p = (a + b)/2 #valor médio do intervalo
        fp = f(p) # calculando f nesse valor médio
        if (fp == 0 or abs((b - a)/2) < err): 
            # caso tenhamos encontrado a raiz ou o erro seja satisfatório, paramos o processo
            return p
        i += 1
        if (fa*fp < 0):
            # parte mais complexa, se f(p) compõe um par com f(a), b deve ser substituído
            b = p
        else:
            # do contrário, a é substitúido, e seu respectivo f(a) por f(p)
            fa = fp
            a = p
        if (i == lim):
            print("Estourou o limite de tentativas")
    return p


#Abaixo temos um exemplo prático visto em aula
def polinomio (x):
    return 2*(x**3) - x**2 + x - 1

print(bisseccao(polinomio, 0, 1, 0.0, 100))