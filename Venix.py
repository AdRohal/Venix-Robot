import random
import datetime

def calculator_robot():
    print("Hello! I'm Venix, your calculator bot. Let's chat about numbers!")
    current_year = datetime.datetime.now().year
    print(f"Venix: I was created in {current_year}.")
    print("You can exit at any time by typing 'exit', 'quit', or 'bye'.")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Venix: Goodbye! If you have more questions, feel free to ask.")
            break

        responses = [
            "Venix: Hmm, interesting. Let's calculate that!",
            "Venix: I'm ready to crunch some numbers! What do you have for me?",
            "Venix: Great! Give me the details, and I'll handle the math.",
            "Venix: Numbers are my language. Fire away!",
        ]

        print(random.choice(responses))

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Venix: Goodbye! If you have more questions, feel free to ask.")
            break

        try:
            result = eval(user_input)
            print(f"Venix: The result is {result}")
        except Exception as e:
            print(f"Venix: Oops! There seems to be an error. {str(e)}")


if __name__ == "__main__":
    calculator_robot()
