def converter(num):
    intermediario = 0
    i = 0
    validador = 0
    resultado = 0
    
    #Vamos trabalhar com a noção de módulo e potenciação
    while (num != 0 and validador == 0):
        # o intermediario recebe o módulo - o resto da divisão por 10, ou seja, o último número
        intermediario = num%10
        # aqui é analisado se o número dado pertence à base 3 ou não, parando o programa
        if intermediario > 2:
            print("Era para ser um valor na base ternária, desconsidere o resultado :(")
            # também é possível o uso de break, mas os profs não gostam muito dele :)
            validador = 1
        # o número precisa ser atualizado em cada iteração sem o seu último dígito, usando o round para isso
        num = num//10
        # por fim, fazemos o cálculo
        resultado += pow(3, i)*(intermediario)
        i += 1
    
    return resultado
    
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

venceu_O = False
venceu_X = False
empate = False

tabuleiro = a + 10*b + 100*c + 1000*d + 10000*e + 100000*f

while (venceu_O == False and venceu_X == False and empate == False) :
    empate = (a != b != c != d != e != f != 0)
    jx_turno = 0
    jy_turno = 0
    
    while (jx_turno == 0 and venceu_O == False and venceu_X == False and empate == False):
        chance = int(input("Jogada do JX: "))
        if (chance == 1 and a == 0 and empate == False):
            a = 1
            jx_turno = 1
        if (chance == 2 and b == 0):
            b = 1
            jx_turno = 1 
        if (chance == 3 and c == 0):
            c = 1
            jx_turno = 1
        if (chance == 4 and d == 0):
            d = 1
            jx_turno = 1
        if (chance == 5 and e == 0):
            e = 1
            jx_turno = 1
        if (chance == 6 and f == 0):
            f = 1
            jx_turno = 1
    
    venceu_O = (a == b == c == 2) or (d == e == f == 2)
    venceu_X = (a == b == c == 1) or (d == e == f == 1)
    tabuleiro = a + 10*b + 100*c + 1000*d + 10000*e + 100000*f
    print("Tabuleiro: ", converter(tabuleiro))
    
    # aqui printa tabuleiro
    
    while (jy_turno == 0 and venceu_O == False and venceu_X == False and empate == False):
        chance = int(input("Jogada do JY: "))
        if (chance == 1 and a == 0):
            a = 2
            jy_turno = 1
        if (chance == 2 and b == 0):
            b = 2
            jy_turno = 1 
        if (chance == 3 and c == 0):
            c = 2
            jy_turno = 1
        if (chance == 4 and d == 0):
            d = 2
            jy_turno = 1
        if (chance == 5 and e == 0):
            e = 2
            jy_turno = 1
        if (chance == 6 and f == 0):
            f = 2
            jy_turno = 1
        
    venceu_O = (a == b == c == 2) or (d == e == f == 2)
    venceu_X = (a == b == c == 1) or (d == e == f == 1)
    tabuleiro = a + 10*b + 100*c + 1000*d + 10000*e + 100000*f
    print("Tabuleiro: ", converter(tabuleiro))
    #aqui printa tabuleiro

# case - switch
print(tabuleiro)
if (venceu_X == True):
    print("Resultado: Venceu JX")
elif (venceu_O == True):
    print("Resultado: Venceu JY")
elif (empate == True):
    print("Empate")