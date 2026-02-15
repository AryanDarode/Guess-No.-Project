import random
n = random.randint(1,100)
num = -1
guesses = 0
while(num!=n):
    
    num = int(input("Guess the Number :- "))
    if(num>n):
        print("Guess the lower number please :- ") 
        guesses += 1
    elif(num<n):
        print("Guess the Higher number please :- ")
        guesses += 1
        
print(f"You have gussed the {num} Number Correctly!! in {guesses + 1} Attempt")






















