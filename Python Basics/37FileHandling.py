f=open('myData.txt','r')

print(f.read())         #reads all  the contents of file
print(f.readline())      #reads the line 1

f1=open('abc','w')
#f1.write("something")

#for copying files
for data in f:
    f1.write(data)

#for image use wb mode    