__author__ = 'nickbortolotti'
#details: initial level example using IF structure

'''
#Case 1: using just a simple IF structure
valor = raw_input("Ingresa un valor general")

if valor < 10:
    print "El valor en menor a 10"
elif valor > 10:
    print "El valor es mayor a 10"
else:
    print "no podemos indentificar el valor real"
'''

'''
#Case 2: comparing switch using dictionary
seleccion = raw_input("Ingresa tu seleccion: ")
print({'demo':1.50,
       'demo1':2.00,
       'demo3':2.50,
       'demo4':3.00}[seleccion])
'''

'''
#Case 3: replacing the Case 2 swicth to If structure
seleccion = raw_input("Ingresa tu seleccion: ")

if seleccion == 'demo':
    print(1.50)
elif seleccion == 'demo1':
    print(2.00)
elif seleccion == 'demo2':
    print (3.00)
else:
    print('mala seleccion')
'''

