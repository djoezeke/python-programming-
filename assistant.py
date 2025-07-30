"""
Simple Personal Assistant - Input/Output Project

This script prompts the user for personal information, summarizes their responses,
and offers the option to save a personalized summary to a text file.

Features:
- Required and randomized optional questions
- Input validation for age and rating
- Summary display with light personalization
- Saves user information to a text file
"""

import random
import datetime

def get_user_data():
    """
    Prompts the user for personal information via required and random optional questions.

    Returns:
        dict: Dictionary containing responses keyed by question identifiers.
    """
    required_questions = [
        ("name", "What is your name? "),
        ("age", "How old are you? ")
    ]

    optional_questions = [
        ("color", "What is your favorite color? "),
        ("food", "What is your favorite food? "),
        ("city", "Which city do you live in? "),
        ("school", "Which SHS did you attend? "),
        ("team", "What is your favorite soccer team? ")
    ]

    selected_optional = random.sample(optional_questions, k=random.randint(2, 4))
    all_questions = required_questions + selected_optional
    responses = {}

    for key, prompt in all_questions:
        while True:
            value = input(prompt).strip()
            if key == "age":
                if value.isdigit() and int(value)> 0:
                    responses[key] = value
                    break
                else:
                    print("Please enter a valid positive number for age.")
            elif value:
                responses[key] = value
                break
            else:
                print("Input cannot be empty. Please try again.")

    return responses

def display_summary(responses):
    """
    Displays a personalized summary of the user's responses.

    Args:
        responses (dict): Dictionary containing user responses.
    """
    print("\n--- Personalized Summary ---")
    print(f"Hello, {responses.get('name', 'Friend')}!")

    age = responses.get('age')
    color = responses.get('color')
    food = responses.get('food')
    city = responses.get('city')
    school = responses.get('school')
    team = responses.get('team')

    if age:
        print(f"You are {age} years old,", end=' ')
    if color:
        print(f"love the color {color},", end=' ')
    if food:
        print(f"and enjoy eating {food}.")
    else:
        print()

    if city:
        print(f"Life must be awesome in {city}!")
    if school:
        print(f"You went to {school} SHS.")
    if team:
        print(f"Go {team}!")

def save_to_file(responses, rating):
    """
    Saves the user's responses and rating to a timestamped text file.

    Args:
        responses (dict): Dictionary containing user responses.
        rating (int): Assistant rating (1 to 5).
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{responses.get('name', 'user')}_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("User Summary\n")
        f.write("============\n")
        for key, value in responses.items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write(f"Rating: {rating}/5\n")

    print(f"✅ Summary saved to {filename}")

def main():
    """
    Main driver function that coordinates user interaction.
    """
    print("👋 Welcome to Your Personal Assistant!\n")

    while True:
        responses = get_user_data()
        display_summary(responses)

        save = input("\nDo you want to save this summary? (yes/no): ").strip().lower()
        if save == "yes":
            while True:
                try:
                    rating = int(input("Please rate this assistant (1 to 5): "))
                    if 1 <= rating <= 5:
                        break
else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Please enter a number.")
            save_to_file(responses, rating)

        again = input("\nWould you like to restart? (yes/no): ").strip().lower()
        if again!= "yes":
            print("👋 Goodbye! Thanks for chatting.")
            break

if __name__ == "__main__":
    main()
