import random

somewords = '''monday apple week ground strict laptop 
mobile headphone pen keyboard mouse
dog cat cricket notebook ground race'''

# Better split (removes extra spaces automatically)
somewords = somewords.split()

word = random.choice(somewords)

if __name__ == '__main__':

    print("Guess the word!")

    letter_guessed = ''
    chances = len(word) + 2

    try:
        while chances > 0:

            print("\nWord:", end=" ")
            for char in word:
                if char in letter_guessed:
                    print(char, end=" ")
                else:
                    print("_", end=" ")

            # Check win condition
            if all(char in letter_guessed for char in word):
                print("\nCongratulations! You won!")
                break

            guess = input("\nEnter a letter to guess: ").lower()

            # Validation
            if not guess.isalpha():
                print("Only letters allowed.")
                continue
            if len(guess) != 1:
                print("Enter only one character.")
                continue
            if guess in letter_guessed:
                print("You already guessed that letter.")
                continue

            letter_guessed += guess

            if guess not in word:
                chances -= 1
                print("Wrong guess!")
                print("Chances left:", chances)

        else:
            print("\nYou lost!")
            print("The word was:", word)

    except KeyboardInterrupt:
        print("\nBye! Try again.")
