import random

comp = random.randint(1, 20)
user = None
#comp = None
guesses = 0

while(user != comp):
    user = int(input("************ Guess a number: ************** \n "))
    print(f"You chose {user}")
    #comp = random.randint(1, 20)
    
    
    if user<=0 or user>=21:
        print("######## Wrong Input ########\n")
    
    elif user < comp:
        print("Please chose a higher number!")
        print(f"Computer chose {comp}\n")
        guesses +=1

    elif user > comp:
        print("Please chose a lower number!")
        print(f"Computer chose {comp}\n")
        guesses +=1   
    
    elif user == comp:
        print(f"Congrats! Computer also chose {comp}")
        print(f"You took {guesses + 1} chances to guess the correct number\n")   #guesses+1 becoz I also included that number of guess in which you answered correctly

with open("Hiscore.txt", "a") as f:
    f.write(str(guesses + 1))
    f.write("\n")  