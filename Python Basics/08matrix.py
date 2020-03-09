from numpy import *

m=matrix('1,2,3;4,5,6;7,8,9')
m1=matrix('7,8,9;1,2,3;4,5,6')
print(m)
print(diagonal(m))
print(m.min())
print(m.max())

m2=m1*m
print(m2)