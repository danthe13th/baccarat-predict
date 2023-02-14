import random

# Initialize past outcomes list
past_outcomes = []

# Define a function to predict the next outcome based on past outcomes
def predict_next_outcome(past_outcomes):
    # Count the number of times "P" and "B" appear in the past outcomes
    num_p = past_outcomes.count("P")
    num_b = past_outcomes.count("B")
    # If "P" has appeared more often than "B", predict "B" for the next outcome
    if num_p > num_b:
        return "B"
    # If "B" has appeared more often than "P", predict "P" for the next outcome
    elif num_b > num_p:
        return "P"
    # If "P" and "B" have appeared an equal number of times, predict either "P" or "B" with equal probability
    else:
        return random.choice(["P", "B"])

# Main loop
while True:
    # Get the user's input for the next outcome and add it to the past outcomes list
    user_input = input("Enter the next outcome (P/B): ")
    past_outcomes.append(user_input)
    # If there are more than 10 past outcomes, remove the oldest outcome to keep the list at a length of 10
    if len(past_outcomes) > 10:
        past_outcomes.pop(0)
    # Predict the next outcome and print it to the console
    next_outcome = predict_next_outcome(past_outcomes)
    print("Next outcome: " + next_outcome)
