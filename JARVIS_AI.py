import time
import random

# =========================
# JARVIS AI
# =========================

print("=====================")
print("      JARVIS AI ")
print("=====================")

# Main Menu
print("1. Chat Bot")
print("2. Mood Detector")
print("3. Calculator")
print("4. Hacker Mode")

# User chooses a mode
choice = input("Choose: ")

# =========================
# CHAT BOT
# =========================

if choice == "1":

    # Welcome message
    print("Jarvis: Hello! I am your AI chatbot.")

    # Infinite chat loop
    while True:

        # User input
        user = input("You: ").lower()

        # Chat responses
        if user == "hello":
            print("Jarvis: Hi BRO.")

        elif user == "how are you":
            print("Jarvis: I'm doing great!")

        elif user == "what is your name?":
            print("Jarvis: My name is Jarvis.")

        # Exit chatbot
        elif user == "bye":
            print("Jarvis: Goodbye.")
            break

        # Unknown message
        else:
            print("Jarvis: I don't understand that yet.")

# =========================
# MOOD DETECTOR
# =========================

elif choice == "2":

    # Happy words list
    happy_words = [
        "happy", "excited", "amazing", "awesome",
        "fantastic", "great", "wonderful",
        "joyful", "cheerful", "proud", "energetic"
    ]

    # Sad words list
    sad_words = [
        "sad", "upset", "depressed", "lonely",
        "disappointed", "hurt", "miserable",
        "crying", "heartbroken", "tired", "hopeless"
    ]

    # Angry words list
    angry_words = [
        "angry", "mad", "furious", "annoyed",
        "frustrated", "aggressive", "mean",
        "irritated", "rude", "offended", "impatient"
    ]

    # User mood input
    text = input("How are you feeling today? ").lower()

    # Detect happy mood
    if any(word in text for word in happy_words):
        print("Mood: Happy 😄")

    # Detect sad mood
    elif any(word in text for word in sad_words):
        print("Mood: Sad 😢")

    # Detect angry mood
    elif any(word in text for word in angry_words):
        print("Mood: Angry 😡")

    # Unknown mood
    else:
        print("Mood: Unknown 🤔")

# =========================
# CALCULATOR
# =========================

elif choice == "3":

    # Import math library
    import math

    # First number
    number_1 = float(input("Enter your first number: "))

    # Math operator
    letters = input("Enter your Letters (-, +, *, %, /): ")

    # Second number
    number_2 = float(input("Enter your number_2: "))

    # Addition
    if letters == "+":
        result = number_1 + number_2

    # Subtraction
    elif letters == "-":
        result = number_1 - number_2

    # Multiplication
    elif letters == "*":
        result = number_1 * number_2

    # Modulus
    elif letters == "%":
        result = number_1 % number_2

    # Division
    elif letters == "/":
        result = number_1 / number_2

    # Invalid operator
    else:
        result = "Invalid operator"

    # Print result
    print(result)

# =========================
# HACKER MODE
# =========================

elif choice == "4":

    # Starting hacker mode
    print("Starting Hacker Mode...")
    time.sleep(1)

    # Fake server connection
    print("Connecting to secret server...")
    time.sleep(1)

    # Searching target IP
    print("Searching target IP...")
    time.sleep(1)

    # Generate fake IP address
    fake_ip = f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"

    # Print fake IP
    print(f"Target IP Found: {fake_ip}")
    time.sleep(1)

    # Fake database access
    print("\nACCESSING DATABASE...\n")

    # Fake hacking progress
    for i in range(0, 101, 10):
        print(f"Hacking... {i}%")
        time.sleep(0.5)

    # Access granted message
    print("\nACCESS GRANTED")
    time.sleep(1)

    # Fake file download
    print("Downloading secret files...")
    time.sleep(2)

    print("Files downloaded successfully.")
    time.sleep(1)

    # Disconnect message
    print("Disconnecting...")
    time.sleep(1)

    print("Hacker Mode Finished 😎")

# Invalid menu choice
else:
    print("Invalid choice.")
