# __len__ method
# class employee:
#     def __init__(self , name):
#         self.name=name
    
#     def __len__(self):
#         i=0
#         for c in self.name:
#             i=i+1
#         return i

# e= employee("rajit")
# print(e.name) 
# print(len(e))


# let we have a class in another file and we import that file in this file
from help import employee
e=employee("harry")

print(str(e))
print(repr(e))
e()
