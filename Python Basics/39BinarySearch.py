pos=-1

def search(list,n):
    l=0
    u=len(list)-1

    while l<=u:
        mid= (l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1       
    return False    


list=[8,17,29,36,45,81]
n=36

if search(list,n):
    print("No is in list at position {}".format(pos+1))
else:
    print("No is not in list")    