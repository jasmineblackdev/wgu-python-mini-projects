import random

number = random.randint(1,10)

print("I'm thinking of a number between 1 and 10.")

# Guess 1
guess1 = int(input("\nGuess #1: "))

if guess1 == number:
    print("🎉 You win!")
elif guess1 > number:
    print("Lower!")
else:
    print("Higher!")


# Guess 2 (only if guess1 is wrong)
if guess1 != number:
    guess2 = int(input("\nGuess #2: "))

    if guess2 == number:
        print("🎉 You win!")
    elif guess2 > number:
        print("Lower!")
    else:
        print("Higher!")


# Guess 3 (only if guess1 AND guess2 are wrong)
if guess1 != number and guess2 != number:
    guess3 = int(input("\nGuess #3: "))

    if guess3 == number:
        print("🎉 You win!")
    else:
        print(f"\n❌ Game over — the number was {number}.")