# def double(x):
#     return x*2

# print(double(5))



#lambda function

# double = lambda x : x*2
# print(double(5))

# cube=lambda x: x**3
# print(cube(5))


# avg = lambda x ,y :(x+y)/2
# print(avg(5,5))

# avg = lambda x ,y ,z :(x+y+z)/3
# print(avg(5,5 ,5))


# we can function as arguments


cube=lambda x: x**3
print(cube(5))

def apply(fx , value):
    return 6+fx(value)

print(apply(lambda x:x*x ,2))