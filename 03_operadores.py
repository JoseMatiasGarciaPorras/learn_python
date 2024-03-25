"""
Tipos de operadores en python:
Aritméticos: + - * / ** // %
Relacionales: <= >= == != < >
Lógicos: and or not
"""
#Aritméticos: Operaciones aritmeticas

#Suma
print(2 + 4)
#Resta
print( 16 - 5)
#Multiplicación
print( 6 * 8)
#División
print(12 / 3)
#Potencia
print(2 ** 2)
#División entera
print(5 // 2)
#Módulo
print(25 % 2)

#Relacionales: Devuelve un valor lógico. Operaciones de comparación

#Menor que
print(5 < 20)
#Mayor que
print(3 > 1)
#Igualdad
print(2 == 2)
#Menor o igual que
print(5 <= 5)
#Mayor o igual que
print(5 >= 3)
#Distinto
print(5 != 10)

#Lógicos: 

#And Solo da True si ambos valores son True
a = True
b = True
c = False
d = False
print(a and b)
print(a and c)
print(d and b)
print(c and d)

#Or: Da True siempre que alguno sea True. Si ambos son False da False
print(a or b)
print(a or c)
print(d or b)
print(c or d)

#Not: Da el contrario. Si es True da False y si es False da True
print(not a)
print(not b)
print(not c)
print(not d)

"""
Gerarquía de operadores:
1. ()
2. % **
3. / // *
4. + -
5. < > <= >= != ==
6. And Or Not
"""