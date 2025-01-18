


def greet(fx):
    def mfx(*args ,**kwargs):
        #args use to take data as tupple
        #kwargs use to take data as dictionary
        print("good mourning")
        fx(*args ,**kwargs)
        print("thanks for using this function")
    return mfx
    

# @greet
def hello():
    print("hello world")

# hello()
greet(hello)()


def add(a,b):
    print(a+b)

greet(add)(2,4)

#wer have to read logging  module