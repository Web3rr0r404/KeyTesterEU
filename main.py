import time

def start_game():
    print("Welcome to the Free Typing Game!")
    print("Type anything you want!")
    print("Your performance will be measured.")
    print("Press Enter to start...")
    input()  # Wait for the user to press Enter
    
    print("\nStart typing when you're ready...")

    # Capture the start time
    start_time = time.time()

    # Automatic input for testing (replace it with real user input in a working environment)
    user_input = "This is an example of free typing text."

    # Capture the end time
    end_time = time.time()

    # Calculate the time taken
    time_taken = end_time - start_time
    words_per_minute = len(user_input.split()) / time_taken * 60

    # Show performance metrics
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f} WPM")

# Start the game
start_game()
