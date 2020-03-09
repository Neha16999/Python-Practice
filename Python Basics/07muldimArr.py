from numpy import *

arr1=array([
            [1,2,3,7,8,9],
            [4,5,6,10,11,12]
])

print(arr1)
print(arr1.dtype)       #to know the type of data
print(arr1.ndim)         #tells dimentions of 
print(arr1.shape)       #gives no of rows and columns

arr2=arr1.flatten()         #converts multidimentional array to single dimentional array
print(arr2)

arr3=arr2.reshape(3,4)      #converts 1d array to nd arr. where 3-no of rows and 4-no of cols
print(arr3)

arr4=arr2.reshape(2,2,3)
print(arr4)