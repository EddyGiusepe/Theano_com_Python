'''
Link para saber executar:
https://www.youtube.com/watch?v=zz9yaeGqyn8

Link de instalação de Pacotes (bibliotecas)
'''

import theano
from theano import tensor

# declare two symbolic floating-point scalars
a = tensor.dscalar()
b = tensor.dscalar()

# create a simple expression
c = a + b

# convert the expression into a callable object that takes (a,b)
# values as input and computes a value for c
f = theano.function([a, b], c)

# bind 1.5 to 'a', 2.5 to 'b', and evaluate 'c'
result = f(1.5, 2.5)
print(result)