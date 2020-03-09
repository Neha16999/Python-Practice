from numpy import *

arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])

arr5=arr1.copy()
print(arr5)         #deep copy
arr1=arr1+10     #adds 5 to every element
print(arr1)

arr3=arr1+arr2
print(arr3)

print(sin(arr1))
print(log(arr2))
print(sum(arr3))
print(sqrt(arr3))

print(concatenate([arr1,arr2]))

arr4=arr3.view()        #view creates array at different memory location #shallo copy
print(arr4)
