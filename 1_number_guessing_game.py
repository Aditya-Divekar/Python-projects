import random 

print("Lets play a word guessing game by usin python , you have 7 chances,'lets play'")

low = int(input("enter th lower no:"))
high = int(input("enter th higher no:"))

print (f"you have 7 cahnces to  guess the correct no between {low} and {high} , 'be prepared'")

num = random.randint(low,high)
chances =7
guess = 0

while guess < chances :
    guess +=   1
    user_guess=int(input("enter your guess :"))

    if user_guess == num:
        print(f"Correct! The number is {num}. You guessed it in {guess} attempts.")
        break

    elif guess == chances and guess !=num:
         print(f"sorry the no was {num} , better luck next time")
   

    elif user_guess < num :
        print("too low , select higher no.")

    elif user_guess > num :
        print("too higher ,select lower no.")