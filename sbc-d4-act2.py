import random

# Get user input and convert to a list of integers
bet = list(map(int, input("Enter your bet (three integers separated by spaces): ").split()))

# Check if the user entered exactly three integers
if len(bet) != 3:
    print("Please enter exactly three integers.")
else:
    # Generate a list of three random integers between 0 and 9
    result = [random.randint(0, 9) for _ in range(3)]
    print(f"Result: {result}")

    # Check if the bet matches the result exactly
    if bet == result:
        print("You Win!")
    # Check if the sorted bet matches the sorted result (same numbers, different order)
    elif sorted(bet) == sorted(result):
        print("You Partially Win!")
    else:
        # If no match, the user loses
        print("You Lose!")