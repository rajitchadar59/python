num = int(input("Enter a number:"))
if(num<50):
    if(num<18):
        print("you are child now!")
    elif(num>=18 and num<=25):
        print("you are young now!")
    else:
        print("you have to married now !")
else:
    print("you areold now")       
