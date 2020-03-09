from array import *

vals=array('i',[2,5,8,9,6])
newArr=array(vals.typecode,(a*a for a in vals))


print(vals)
print(vals.buffer_info())       #address and size

#for i in range(len(vals)):
 #   print(vals[i])

for e in newArr:
    print(e)    