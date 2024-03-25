a = input('Introduce un número: ')
print('El valor que has elegido es : ', a)

#Suma de dos números
#Input toma los valores de entrada como strings
#Por lo que concatena ambos números

print('Vamos a sumar dos valores concatenendo')
a = input('Introduce el primer número: ')
b = input('Introduce el segundo número: ')
print(f'La suma de {a} más {b} es {a + b}', type(a + b))

#PAra evitar esto hay que castear las variables a tipo entero

print('Vamos a sumar dos valores casteando')
a = int(input('Introduce el primer número: '))
b = int(input('Introduce el segundo número: '))
print(f'La suma de {a} más {b} es {a + b}', type(a + b))

#Se puede castear de entero a texto, a flotante, etc
"""
Otra forma de asegurarnos que una variable es del tipo que 
queremos, es usar tipado estático. Por defecto, python
usa tipado dinámico, pero podemos forzar el tipado 
estático. 
"""

#Tipado dinámico
num = 25

#Tipado estático
num: int = 25