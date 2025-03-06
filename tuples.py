import numpy as np

q = ['-1', '', '']
w = ['-2', '', '']
e = ['-3', '', '']
r = ['-4', '', '']
t = ['-5', '', '']
y = ['-6', '', '']
u = ['-7', '', '']
i = ['-8', '', '']
o = ['-9', '', '']
p = ['-10', '', '']

a = ['', '-1', '']
s = ['', '-2', '']
d = ['', '-3', '']
f = ['', '-4', '']
g = ['', '-5', '']
h = ['', '-6', '']
j = ['', '-7', '']
k = ['', '-8', '']
l = ['', '-9', '']

z = ['', '', '-1']
x = ['', '', '-2']
c = ['', '', '-3']
v = ['', '', '-4']
b = ['', '', '-5']
n = ['', '', '-6']
m = ['', '', '-7']

list = []
list.append(d)
list.append(d)
list.append(g)
list.append(g)
list.append(r)
list.append(r)

matrix = np.array(list)
matrix_transposed = matrix.T

np.savetxt('tablatura.csv', matrix_transposed, delimiter=',', fmt='%s')