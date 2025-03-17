while True:
    x = open("file1.txt","r")
    c = len(x.readlines())
    x.close()
    i=input("For adding content press a, for reading press r, and to exit press any button :: ")
    if(i=='a' or i=="A"):
        a=open("file1.txt","a")
        i1=input("Add ur interests :: ")        
        a.write(f"Interest {c+1} :: {i1}")
        print("Success")
        a.close()
    elif(i=="r" or i=="R"):
        a=open("file1.txt","r")
        print(a.read())
        a.close()
    else:
        print("Thank you!!!!")
        break