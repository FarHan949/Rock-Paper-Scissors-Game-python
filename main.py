import random


computer =  random.choice([-1, 0, 1])

revers_dict = {-1: "Scissor", 0: "Rock", 1: "Paper"}

# print(computer)

youChose =  input("Enter a chose rock = r, paper = p, scissors = s : ")

your_dict  = {"s": -1, "r" : 0, "p": 1}

you = your_dict[youChose]

print(f"You chose {revers_dict[you]}\n Computer chose {revers_dict[computer]}")


if (computer  == you):
    print("It's a tie")
    
else:
    if (computer == -1 and you == 1):
        print("You lose")
    elif (computer == -1 and you == 0):
        print("You win")
    elif (computer == 0 and  you == 1):
        print("You win")
    elif (computer == 0 and  you == -1):
        print("You lose")
    elif (computer == 1 and  you == -1):
        print("You win")
    elif (computer == 1  and  you == 0):
        print("You lose")
    else:
        ("Something is wrong")








