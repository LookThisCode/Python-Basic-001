__author__ = 'nickbortolotti'

from sys import argv

script, usuario = argv
prompt = '> '

print "Hola %s yo el %s" % (script, usuario)
print "tengo para hacerle algunas preguntas"
print "le parezco lindo yo %s?" % usuario
gusto = raw_input(prompt)
print "donde vive usted %s?" % usuario
vivir = raw_input(prompt)
print "que tipo de computadora tiene %s" % usuario
computadora = raw_input(prompt)
print """
Perfecto!, %r,%r,%r
""" % (gusto,vivir,computadora)