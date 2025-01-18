# def cube(x):
#     return x*x*x
# print(cube(2))

# l =[1,2,3,4,6,8]
# # newl=[]
  
# # for item in l:
# #     newl.append(cube(item))

# # print(newl)  

# newl = list(map(cube ,l))
# print(newl)


# #FILTER

# def filter_func(a):
#     return a>4

# newnl=list(filter(filter_func ,l))
# print(newnl)
      
#REDUCE

from functools import reduce

l=[10,11,15,4]

sum = reduce(lambda x ,y :x+y , l)
print(sum)