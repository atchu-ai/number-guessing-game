import random

number = random.randint(1, 10)
attempts = 3

print("🎮 Welcome to Number Guessing Game!")
print("You have 3 attempts to guess the number.")

while attempts > 0:
    guess = int(input("Enter your guess (1-10): "))

    if guess == number:
        print("🎉 Correct! You won!")
        break
    elif guess > number:
        print("📉 Too high!")
    else:
        print("📈 Too low!")

    attempts -= 1
    print("Attempts left:", attempts)

if guess != number:
    print("😢 Game Over!")
    print("The correct number was:", number)
