# class employee:
#     def __init__(self):
#         self.name="rajit"

# a= employee()
# print(a.name)

#access modifier
#private
#name mangling
class employee:
    def __init__(self):
        self.__name="rajit"

a= employee()
# print(a.__name)
print(a._employee__name)


#protected

class employee:
    def __init__(self):
        self.__name="rajit"


class  student(employee):
    def _print(self):
        print("hi")
a= employee()
s=student()
s._print()