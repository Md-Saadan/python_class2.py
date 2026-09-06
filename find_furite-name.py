import random
furit=["Banana","water Melon","Orange","Apple","Blue Berry","Musk Melon","Pine Apple","Strowberry","Fig","Custared Apple"]
furit_name=random.choice(furit)
print(furit_name)

count=0
score=100
while(count<5):
    guess=input("Enter a furit Name")
    if guess==furit_name:
        print("You Won!")
        print("points",points)
        break
    else:
        if count==0:
            print("Hint1:length of furit is",len(furit_name))
        elif count==1:
            print("Hint2:Frist Latter of Furit is",furit_name[0])
        elif count==2:
            Hint3=furit_name[0]
            for i in range(len(furit_name)-1):
               Hint3+="*"
            print("Hint3:The Furit Name Could Count Be",Hint3)
        elif count==3:
            Hint4=furit_name[0]
            for i in range(len(furit_name)-2):
                Hint4="*"
            Hint4+=furit_name[-1]
            print("Hint4:The Furit Name Cold Be",Hint4)
        else :
            pass
    count+=1
    points=-20    

            



