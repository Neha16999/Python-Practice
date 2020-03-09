from numpy import *

arr=array([1,2,3,4,5.0],float)      #float was not mandetory

print(arr.dtype)

#creating array using linespace
arrr=linspace(0,15,16)  #start,end, no of partitions
print(arrr)

#creating using arange
arr1=arange(1,15,2)         #start,end,steps(difference)
print(arr1)

#using logspace where values are separated on the basis of log
arrl=logspace(1,4,40)
print(arrl)

#zeros- gives array with mention no of zeros
arrz=zeros(5) # by default flaot for int use zeros(no_of_zeros,int)
print(arrz)

#ones- gives array with mention no of ones
arro=ones(6,int)
print(arro)
