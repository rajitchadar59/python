

st=input("enter message")
words=st.split(" ")
coading =int(input("enter the mode 0 for decoding 1 for coding"))

if(coading):
        nwords=[]
        for word in words:
               
            if(len(word)>=3):
                r1="gfe"
                r2="thg"
                strn=r1+word[1:]+word[0]+r2
                nwords.append(strn)
                
            else :
                nwords.append(word[::-1])

        print(" " .join(nwords))
else:
    nwords=[]
    for word in words:
               
        if(len(word)>=3):
            strn=word[3:-3]
            strn=strn[-1] +strn[:-1]
            nwords.append(strn)
                
        else :
            nwords.append(word[::-1])
    print(" " .join(nwords))        
     
    

