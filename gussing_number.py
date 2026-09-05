import random
hidden_number=random.randint(1,100)
score=100

for i in range(5):
    guess=int(input("Guessing a number"))
    if guess==hidden_number:
        print("You Won!")
        print("score:",score)
        break
    elif guess>=hidden_number:
        print("Hint!:Your guess is heigh")
        score-=20
    else:
        print("Your guess is low")
        score-=20
else:
    print("All Chanes are gone!")
    print("You lost!")
    print("Hidden number:",hidden_number)
            