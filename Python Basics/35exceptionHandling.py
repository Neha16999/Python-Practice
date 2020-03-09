a=5
b=2

try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter a no : "))
    print(k)

except ZeroDivisionError as e:
    print("Cant divide a no by Zero")

except ValueError as e:
    print("invalid input")

except Exception as e:      #any other exception
    print("Something went wrong...")

finally:
    print("Resource closed")
    
          
