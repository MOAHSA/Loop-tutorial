import random  
target = random.randint(1, 10)  
while True:  
    guess = int(input("Guess the number (1-10): "))  
    if guess == target:  
        print("You guessed it!")  
        break  
    print("Try again!")  
