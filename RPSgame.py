import random
options=("Rock","Paper","Scissors")
player=None
running=True
while running:
    comp=random.choice(options)
    
    while player not in options:
        player=input("Enter a choice:").lower()
        if player == 'q':  # Allow quitting
            running = False
            break
    

print(player)
print(comp)

if player==comp:
    print("Its a tie")
elif player=='rock' and comp=='scissors':
    print("You win")
elif player=="scissors" and comp=="paper":
    print("You win")
elif player=="paper" and comp=="rock":
    print("you win")

else:
    print("You lose")