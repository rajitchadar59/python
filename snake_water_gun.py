import random

def check(user ,comp):
    if(comp==user):
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1
    
    return 1



comp = random.randint(0,2)
user = int(input("  0 for snake  1 for water 2 for gun: \n"))

score = check(user ,comp)
print("you -> " ,user)
print("computer-> " ,comp)
if(score==0):
    print("its a draw")
elif(score==1):
    print("you  won")  

else:
    print("you loss")     



