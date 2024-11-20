import random

# Step 1: list of random questions
questions = [
    "What is your favorite color?",
    "If you could have any superpower, what would it be?",
    "What is your dream vacation destination?",
    "Do you prefer tea or coffee?",
    "What is your favorite book?",
    "If you could meet anyone, dead or alive, who would it be?",
    "What is your favorite movie?",
    "What hobby have you always wanted to pick up?",
    "What is your favorite food?",
    "Where do you see yourself in five years?"
]

# Step 2:  responses
responses = [
    "Oh wow, that's so cool! 😊",
    "I didn't expect that! You're full of surprises! 💖",
    "Aww, that's amazing! Tell me more! 🥰",
    "You're so interesting! I could talk to you all day! 😍",
    "That's such a wonderful answer! 🌸",
    "Wow, you're really unique! I love it! 💫",
    "Haha, you're making me smile with that! 😊",
    "I bet you have lots of stories about that! 😃",
    "You're so fun to chat with! 💬✨",
    "Ooh, I like how you think! 💡"
]

# Step 3: Define the chatbot function
def hansika():
    print("Hello! I am Hansika, your friendly chatbot! 😊")

    while True:
        # Randomly select a question from the list
        question = random.choice(questions)
        print("\nHansika: " + question)

        # Get user's response
        response = input("You: ")

        # Option to exit the chat
        if response.lower() in ['exit', 'quit', 'bye']:
            print("Hansika: It was so nice chatting with you! Take care, my friend! 💖👋")
            break
        else:
            # random response
            hansika_response = random.choice(responses)
            print(f"Hansika: {hansika_response}")

# Run the chatbot
hansika()
