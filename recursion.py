#factorial 7*6*5*4*3*2*1
#factorial[0]=1

# factorial n = n * factorial(n-1)

# def  factorial(n):
#     if(n==0 or n ==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    

# print(factorial(5))       
    
f0=0
f1=1
def fibonacci(n ,a ,b):
    if(n==0):
        return
    c=a+b
    print(c ,end=" ")
    fibonacci(n-1 ,b ,c)


fibonacci(5 ,f0 ,f1)    