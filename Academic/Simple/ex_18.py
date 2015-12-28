__author__ = 'nbortolotti'

if __name__ == '__main__':
    x = raw_input("ingresa valor 1: ")
    y = raw_input("ingresa valor 2: ")
    print(x, y)

def print_dos(*args):
    arg1, arg2 = args
    print "argumento1: %r, argumento2: %r" % (arg1, arg2)

    
