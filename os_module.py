import os
# if( not os.path.exists("data")):
#     os.mkdir("data") # a folder is created


# folder ke andar folder 


# for i in range(0 ,100):
#     os.mkdir(f"data/day{i+1}")



# for i in range(0 ,100):
#     os.rename(f"data/day{i+1}" ,f"data/tutorial{i+1}")
    
# want to rename second time
# for i in range(0 ,100):
#     os.rename(f"data/tutorial{i+1}" ,f"data/tutorial__{i+1}")    



#gives folder inside the folder
folders = os.listdir("data")



# print(folders)folders
# for folder in  folders :
#     print(folder)

# for folder in  folders :
#     print(folder)
#     print(os.listdir(f"data/{folder}"))  give file inside the folder




#  in which directory you are now !!
print(os.getcwd())


#to chage the directory
os.chdir("/python")
print(os.getcwd())

