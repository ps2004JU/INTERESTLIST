print("Welcome to My Interest List")
while True:
    x = open("MYF.txt","r")
    c = len(x.readlines())
    x.close()
    i=input("For adding content press a, for reading press r, and to exit press any button :: ")
    if(i=='a' or i=="A"):
        a=open("MYF.txt","a")
        i1=input("Add ur interests :: ")        
        a.write(f"\nInterest no - {c+1} : {i1}")
        print("Success")
        a.close()
    elif(i=="r" or i=="R"):
        a=open("MYF.txt","r")
        print(a.read())
        a.close()
    else:
        print("Thank you!!!! Have a nice day")
        break