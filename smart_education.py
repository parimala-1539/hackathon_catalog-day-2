import random
import time

# Data: States and Capitals
states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata",
}

# Function to generate multiple-choice options
def generate_options(correct_answer):
    options = [correct_answer]
    while len(options) < 4:
        option = random.choice(list(states_and_capitals.values()))
        if option not in options:
            options.append(option)
    random.shuffle(options)
    return options

# Function to run the quiz
def quiz():
    score = 0
    total_questions = 5  # Number of questions in the quiz

    states = list(states_and_capitals.keys())
    random.shuffle(states)

    start_time = time.time()

    for i in range(total_questions):
        state = states[i]
        correct_capital = states_and_capitals[state]
        options = generate_options(correct_capital)

        print(f"\nQuestion {i + 1}: What is the capital of {state}?")
        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")

        try:
            answer = int(input("Choose the correct option (1-4): ").strip())
            if options[answer - 1].lower() == correct_capital.lower():
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {correct_capital}.\n")
        except (ValueError, IndexError):
            print(f"Invalid input! The correct answer is {correct_capital}.\n")

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    print(f"\nQuiz Over! Your final score is {score}/{total_questions}.")
    print(f"You completed the quiz in {time_taken} seconds.")

    return score, time_taken

# Function to display the leaderboard
def update_leaderboard(score, time_taken, leaderboard):
    name = input("Enter your name to save your score: ").strip()
    leaderboard.append((name, score, time_taken))
    leaderboard.sort(key=lambda x: (-x[1], x[2]))  # Sort by score, then by time

    print("\n--- Leaderboard ---")
    for idx, entry in enumerate(leaderboard):
        print(f"{idx + 1}. {entry[0]} - Score: {entry[1]}, Time: {entry[2]} seconds")

if __name__ == "__main__":
    leaderboard = []
    while True:
        score, time_taken = quiz()
        update_leaderboard(score, time_taken, leaderboard)

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break
