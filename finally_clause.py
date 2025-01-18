def func1():
    try:
        l=[1,2,3,4,5]
        i = int(input("enter index"))
        print(l[i])
        return 1
    except:
        print("some error occur")
        return 0
    finally:
        print("i am always exicuted!!!")

x= func1()
print(x)