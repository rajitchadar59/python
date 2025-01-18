a= (input("enter the number"))
print(f"the multiplication table of {a}")
try:
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
        print(e)       

     


print("some imp lines of code")
print("end of program")