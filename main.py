import random
import os

HIGH_SCORE_FILE = "high_scores.txt"


def roll_dice():
    """Simulates rolling two dice and returns their total."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


def load_high_scores():
    """Loads high scores from a file."""
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    with open(HIGH_SCORE_FILE, "r") as file:
        return int(file.read().strip())


def save_high_score(score):
    """Saves the high score to a file."""
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))


def guessing_game():
    print("Welcome to the Dice Guessing Game!")
    print("Two dice will be rolled, and you need to guess their total (between 2 and 12).")

    high_score = load_high_scores()
    print(f"Current High Score: {high_score}\n")

    score = 0
    play_again = True

    while play_again:
        dice_total = roll_dice()
        attempts = 3

        while attempts > 0:
            try:
                guess = int(input(f"\nYou have {attempts} attempt(s) left. Enter your guess: "))
                if guess < 2 or guess > 12:
                    print("Invalid guess! The total of two dice can only be between 2 and 12.")
                    continue

                if guess == dice_total:
                    print(f"Congratulations! You guessed it right. The total was {dice_total}.")
                    score += 1
                    break
                elif guess < dice_total:
                    print("Too low!")
                else:
                    print("Too high!")

                attempts -= 1
            except ValueError:
                print("Please enter a valid number.")

        if attempts == 0 and guess != dice_total:
            print(f"Sorry, you've run out of attempts. The correct total was {dice_total}.")

        print(f"\nYour current score is: {score}")

        if score > high_score:
            print(f"New High Score! Your score of {score} beats the previous high score of {high_score}.")
            high_score = score
            save_high_score(high_score)

        play_again_input = input("\nDo you want to play another round? (yes/no): ").lower()
        play_again = play_again_input.startswith('y')

    print(f"\nThanks for playing! Your final score is: {score}")
    print(f"High Score: {high_score}")


if __name__ == "__main__":
    guessing_game()

