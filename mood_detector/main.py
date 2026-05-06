happy_words = ["Happy", "Excited", "Amazing", "Awesome","Fantastic", "Great", "Wonderful", "Joyful", "Cheerful" ,"Proud", "Energetic"]
sad_words = ["sad", "Upset", "Depressed" ,"Lonely", "Disappointed", "Hurt", "Miserable", "Crying", "Heartbroken", "Tired", "Hopeless"]
angry_words = ["angry", "mad", "Furious", "Annoyed", "Frustrated", "Aggressive","Mean", "Irritated", "Rude", "Offended", "Impatient"]

text = input("How are you feeling today? ").lower()

if any(word in text for word in happy_words):
    print("Mood: Happy 😄")

elif any(word in text for word in sad_words):
    print("Mood: Sad 😢")

elif any(word in text for word in angry_words):
    print("Mood: Angry 😡")

else:
    print("Mood: Unknown 🤔")
