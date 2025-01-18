import time
current_time = time.strftime("%H:%M:%S")
print(current_time)

hour =int(time.strftime("%H"))
if(hour > 0 and hour <=12):
    print("good mourning ! ")
elif(hour >12 and hour <17):
    print("good afternoon sir !")    

elif(hour >=17 and hour < 19):
    print("good evening sir !")

if(hour >=19 and hour <=24):
    print("good night sir  bahut time ho gaya so jao! ")         