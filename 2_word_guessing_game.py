import random

name = input("What is your name? ")
print("Good Luck!", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("\nGuess the characters:")

guesses = ""
turns = 12

while turns > 0:
    failed = 0

    
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()  

    
    if failed == 0:
        print("You Win!")
        print("The word is:", word)
        break

    guess = input("Guess a character: ").lower()

    if len(guess) != 1:
        print("Please enter only one character.")
        continue

    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses += guess

    # If wrong guess
    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", turns, "guesses left.")

        if turns == 0:
            print("You Lose!")
            print("The word was:", word)
