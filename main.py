Questions=("What has to be broken before you can use it?","What is full of holes but still holds water?")
Q1_amount=100
Q2_amount=200
Q3_amount=300
Q4_amount=400
Q5_amount=1400
Q6_amount=1500
Q7_amount=1600
Q8_amount=1700
Q9_amount=1800
Q10_amount=2800
Q11_amount=2900
Q12_amount=3000
Q13_amount=3100
Q14_amount=3200
Q15_amount=4000
amount=(Q1_amount,Q2_amount,Q3_amount,Q4_amount,Q5_amount,Q6_amount,Q7_amount,Q8_amount,Q9_amount,Q10_amount,Q11_amount,Q12_amount,Q13_amount,Q14_amount,Q15_amount)


print("Hello, welcome to Guess the word game")
name=input("Introduce yourself to the audience!")
print("Welcome"+" "+name+" "+"nice to meet you")
print("Are you good at guessing words? 1: i'm really good at it, 2:i will try my best, 3:no, but i will just play")
if answer==1:
    print("you might find it easy")
elif answer==2:
    print("i hope you win")
elif answer==3:
    print("i hope at least you guess the first 5 riddles")


for index in range(len(Questions)):
    Q=Questions[index]
    print(Q)
    answers=input("What is the word?")
    answer=egg
    if answer==ANSWERS[index]:
        print("That's right",Amount[index])
    else:
        print("Oh sorry, wrong answer")
        break

