import random

secret_word = ["gym", "weights", "cardio"]
random_secret_word = random.choice(secret_word)

print(f"This word has {len(random_secret_word)} letters. \n")

user_guess = input("Guess the word: ").lower() #first attempt
if user_guess == random_secret_word:
    print("Congratulations you Won!")
else:
    user_guess2 = input("Guess the word: ").lower() #second attempt
    if user_guess2 == random_secret_word:
     print("Congratulations you Won!")
    else:
        user_guess3 = input("Guess the word: ").lower() #third attempt
        if user_guess3 == random_secret_word:
            print("Congratulations you Won!")
        else:
            print("I'm sorry you guessed incorrectly, please try again.")
