import random

list=['Stone','Paper','Scissors']

print("-----Let's play Stone Paper Scissors game with computer.-----")
rounds=int(input("Enter the number of rounds you want to play: "))
print("Choose any one from the following:")
print("1 for Stone\n2 for Paper\n3 for Scissors")

comp_score=0
user_score=0

n=0
while n<rounds:
    comp=random.choice(list)

    user=input("Enter your choice: ")
    if (comp=='Stone'and user=='1') | (comp=='Paper'and user=='2') | (comp=='Scissors'and user=='3'):
        print("Computer's choice is: ",comp)
        print("It's a tie!")
    #    comp_score=0
    #    user_score=0
    elif (comp=='Stone' and user=='2') | (comp=='Paper' and user=='3') | (comp=='Scissors' and user=='1'):
        print("Computer's choice is: ",comp)
        print("You won!")
        user_score+=1
    else:
        print("Computer's choice is: ",comp)
        print("You lose!")
        comp_score+=1
    print(f"Computer's score: {comp_score} and Your score: {user_score}")
    # print("Your score: ",user_score)
    n+=1


if comp_score>user_score:
    print(f"Computer won the game with {comp_score} points.")
elif comp_score<user_score:
    print(f"Congratulations! you won the game with {user_score} points.")    
else:  
    print("The Game was too clso but it's a tie!")
print("-----------------------Game Over-----------------------")