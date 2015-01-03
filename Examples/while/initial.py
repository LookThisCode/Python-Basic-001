__author__ = 'nickbortolotti'

'''
#Case 1: using a while loop to test a number section
a = 0
b = int(raw_input("Ingresa tu seleccion: "))

while a < b:
    print(a)
    a+=1 
'''    
'''    
#Case 2: loop counting in reverse excluding modulus - using continue
b = int(raw_input("Ingresa tu seleccion: "))

while b:
    b = b-1
    if b % 2 != 0: continue
    print(b)
'''

'''
#Case 3: loop using break
while True:
    nombre = raw_input("Ingresa tu nombre: ")
    if nombre == 'stop':break
    edad = raw_input("Ingrese su edad: ")
    print('Hola ', nombre, '==', int(edad) ** 2)
'''