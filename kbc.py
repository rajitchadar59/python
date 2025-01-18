questions =[["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],        
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],   
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],
            ["which language was usedd to create facebook ?" ,"python" ,"french" ,"javascript" ,"php"  ,4],
            
            ]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,32000]
money =0
for i in range(0 , len(questions)):
    question = questions [i]
    print(f"\n\nQuestions for rs. {levels[i]}")
    print("Q1.",question[i])
    print(f"1.{question[1]}              2. {question[2]}   ")
    print(f"3.{question[3]}              4. {question[4]}   ")
    reply=int(input("enter your answar (1-4)"))
    if(reply== question[-1]):
        print(f"correct answar , you have won {levels[i]} ")
        
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
             

    else:
        print("wrong answar")
        break
print(f"your takehome money is {money}")    


