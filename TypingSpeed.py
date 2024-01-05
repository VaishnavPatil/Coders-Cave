import random
import time

def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and challenging.",
        "Practice makes perfect.",
        "Coding is an essential skill in today's world.",
        "Type as fast as you can!"
    ]
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, typed_words):
    total_time_seconds = end_time - start_time
    words_per_minute = (typed_words / total_time_seconds) * 60
    return words_per_minute

def get_feedback(typing_speed):
    if typing_speed < 30:
        return "You can improve your typing speed! Keep practicing."
    elif 30 <= typing_speed < 50:
        return "Good effort! Your typing speed is improving."
    elif 50 <= typing_speed < 70:
        return "Great job! You have a decent typing speed."
    else:
        return "Excellent! You have an impressive typing speed."

def main():
    print("Welcome to the Typing Speed Tester!")

    input("Press Enter to start...")

    sentence = generate_random_sentence()
    print("\nType the following sentence:\n")
    print(sentence)

    input("Press Enter when you are ready to start typing...")

    start_time = time.time()
    user_input = input("\nStart typing here: ")
    end_time = time.time()

    typed_words = len(user_input.split())
    typing_speed = calculate_typing_speed(start_time, end_time, typed_words)

    print("\nTyping Speed: {:.2f} words per minute".format(typing_speed))
    feedback = get_feedback(typing_speed)
    print("Feedback:", feedback)

if __name__ == "__main__":
    main()
