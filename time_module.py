import time
def usingwhile():
    i=0
    while i<5000:
        i=i+1
        print(i)
   

def usingfor():
    for i in range(5000):
        print(i)

# init= time.time()
# usingwhile()
# t2=time.time()-init
# usingfor()
# print(time.time()-init)
# print(t2)


# print(4)
# time.sleep(1)
# print(5)
t=time.localtime()
formatedtime=time.strftime("%d-%m-%y  %H:%M:%S" )
print(formatedtime)
print(t)