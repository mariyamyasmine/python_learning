def games():
option = ["rock", "paper", "scissor"]
user1 = input("Enter your move (rock, paper, scissor): ") 
user2 = input("Enter your move (rock, paper, scissor): ") 
if user1 not in option:
    print("Invalid input! Please choose rock, paper, or scissor.")
    if user2 not in option:
        print("Invalid input! Please choose rock, paper, or scissor")
elif user1 == user2:
    print("It's a tie!")
elif(user1 == "rock" and user2 == "scissor"):
    print("user1 wins!")
elif(user1 == "paper" and user2 == "rock"): 
    print("user1 wins!")
elif(user1 == "scissor" and user2 == "paper"):
    print("user1 wins!")
elif(user1 == "rock" and user2 == "paper"):
    print("user2 wins!")
elif(user1 == "scissor" and user2 == "rock"):
    print("user2 wins!")
elif(user1 == "paper" and user2 == "scissor"):
    print("user2 wins!")
elif(user1 == "rock" and user2 == "paper"):
    print("user2 wins!")
else:
    print("invalid input")
    
games()    

print("Game starts")