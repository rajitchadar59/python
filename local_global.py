# x=4 #global 
# print(x)

# def hello():
#     x=5 #local
#     print(x)
#     print("hello rajit")

# hello()
# print(f"the global x is {x}")



x=4
print(x)

def hello():
    global x
    x=10    
    print(x)
    print("hello rajit")

hello()
print(f"the global x is {x}")