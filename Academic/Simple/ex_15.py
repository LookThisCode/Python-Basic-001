__author__ = 'nickbortolotti'

from sys import argv
script, archivo = argv

txt = open(archivo)

print "Aqui tenemos su archivo %s:" % archivo
print txt.read()

print "Repita el nombre del archivo nuevamente:"
archivo_again = raw_input("> ")

txt_again = open(archivo_again)

print txt_again.read()
