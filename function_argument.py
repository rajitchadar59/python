
# default argument

# def avrage(a=1,b=3):
#     print("The avrage is : ",(a+b)//2)

# avrage( 1,1)   

# keyword argument

# def avrage(a=1,b=3):
#     print("The avrage is : ",(a+b)//2)

# avrage(b=10 , a= 5)    

# //requrired arguments

# def avrage(a,b=3):
#     print("The avrage is : ",(a+b)//2)

# avrage(1)


# veriable length argument

# arguments as a tupple
def avrage(*numbers):
    sum=0
    for i in numbers:
        sum = sum+i
   
    return sum/len(numbers)

c=avrage(5,6 ,7 ,1)   
print(c)



