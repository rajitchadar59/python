# x=int(input("Enter the value of x"))

# match x:
#     case 0:
#         print("number is zero")
#     case 4:
#         print("number is 4") 
#     case _:
#         print(x)

x=int(input("Enter the value of x"))

match x:
    case 0:
        print("number is zero")
    case 4:
        print("number is 4") 
    case _ if x>90:
        print("x >90")
    case _ if x==90:
        print("x is 90")    
    case _:
        print(x)    
