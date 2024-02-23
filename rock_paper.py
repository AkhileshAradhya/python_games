import random
user_wins = 0
computer_wins = 0
user_name =input(" Enter Your Name ::")
print("Welcome ",user_name," to play ROCK-PAPER-SCISSOR" )
options = ["rock" , "paper" , "scissor"]

while True:
    user_input = input("type 'rock\paper\scissor' or 'q' to quit : ").lower()
    if user_input == "q":
       break
       # quit()

    if user_input not in ["rock" , "paper" , "scissor"]:
        continue

    random_number = random.randint(0,2)
    #rock = 0 ::paper = 1 ::scissor = 2
    computer_pick =options[random_number]
    print("Computer Picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print(user_name,"YOU WON !!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print(user_name, "YOU WON !!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print(user_name, "YOU WON !!")
        user_wins += 1
    elif user_input == computer_pick:
        print(user_name , "it's DRAW !!")
    else:
        print(user_name,"YOU LOST !!")
        computer_wins += 1
print("YOU WON :",user_wins,"TIMES")
print("COMPUTER WON : ",computer_wins,"TIMES")
if user_wins > computer_wins:
    win= user_wins-computer_wins
    print("CONGRATES",user_name,"YOU BEAT COMPUTER BY :",win,"SCORE")
else:
    win = computer_wins-user_wins
    print("BETTER LUCK NEXT TIME",user_name,"COMPUTER WON BY :",win,"SCORE")
print("Goodbye!")
