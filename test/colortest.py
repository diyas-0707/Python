import random

# List of colors to choose from
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

def generate_cards():
    """Generate two cards with random color names and text colors."""
    card1_name = random.choice(COLORS)
    card1_color = random.choice(COLORS)
    card2_name = random.choice(COLORS)
    card2_color = random.choice(COLORS)
    return card1_name, card1_color, card2_name, card2_color

def play_round(round_num):
    """Play a single round of the game."""
    print(f"\n--- Round {round_num} ---")
    card1_name, card1_color, card2_name, card2_color = generate_cards()

    # Display cards
    print(f"Card 1: The text says '{card1_name}' but is colored '{card1_color}'.")
    print(f"Card 2: The text says '{card2_name}' but is colored '{card2_color}'.")

    # Get user input
    while True:
        user_input = input("Does the color name on Card 1 match the text color on Card 2? (yes/no): ").strip().lower()
        if user_input in ["yes", "no"]:
            break
        print("Invalid input! Please enter 'yes' or 'no'.")

    # Check the answer
    correct = card1_name == card2_color
    if (user_input == "yes" and correct) or (user_input == "no" and not correct):
        print("Correct!")
        return 1  # Player scores a point
    else:
        print("Wrong!")
        return 0  # No points

def main():
    """Main function to run the game."""
    print("Welcome to the Color Matching Game!")
    print("You will play 10 rounds. Try to get as many correct as possible.")
    
    score = 0
    max_rounds = 10

    for round_num in range(1, max_rounds + 1):
        score += play_round(round_num)

    print("\n--- Game Over ---")
    print(f"Your final score is: {score}/{max_rounds}")

if __name__ == "__main__":
    main()