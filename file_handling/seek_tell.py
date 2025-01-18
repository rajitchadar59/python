# with open("file_handling/file.txt" ,"r") as f:
#         print(type(f))
#         f.seek(10)
#         print(f.tell())
#         data=f.read(5)
     
#         print(data)


with open("file_handling/hello.txt" ,"w") as f:
    f.write("hello rajit")
    f.truncate(5)