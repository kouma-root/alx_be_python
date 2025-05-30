import random
secret_number = random.randint(1, 10)
correct = False
again = 1
count = 0
print("Welcome to the Guessing Game!")
while again == 1:
    while not correct :

            guess = int(input("Guess a number between 1 and 10:"))
            if guess > secret_number :
                    print(" Oops, your guess is a bit high. Try again!")
                    count += 1
            elif guess < secret_number :
                    print(" Nope, your guess is a bit low. Give it another shot!")
                    count += 1
            else :
                    print(" Congratulations! You guessed it!", count, "tries.")
                    correct = True
    again = input("Do you want to play again? (1/0): ")