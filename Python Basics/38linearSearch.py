pos=-1
def search(list, n):
    for i in range (len(list)):
        if list[i]==n:
            globals ()['pos'] = i
            return True


list=[18,8,7,9,6]
n=18

if search(list,n):
    print("No is in list at position {}".format(pos+1))
else:
    print("No is not in list")    