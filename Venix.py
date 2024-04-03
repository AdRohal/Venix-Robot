import tkinter as tk
import random
import datetime
import time


class CalculatorRobot:
    def __init__(self, master):
        self.master = master
        master.title("Venix - Your Calculator Bot")
        self.center_window()
        self.create_widgets()

    def center_window(self):
        self.master.update_idletasks()  # Update the window to calculate its size
        # Get the screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.master.winfo_width()) // 2
        y = (screen_height - self.master.winfo_height()) // 2

        # Set the geometry of the window
        self.master.geometry("+{}+{}".format(x, y))

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text="Venix", font=("Arial", 24, "bold"), fg="blue")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.grid(row=1, column=0, columnspan=2, padx=10)
        self.result_text.tag_config("venix", background="skyblue", foreground="black")
        self.result_text.tag_config("user", background="yellow", foreground="black")

        self.input_label = tk.Label(self.master, text="You:")
        self.input_label.grid(row=2, column=0, sticky="w", padx=(10, 0))

        self.input_entry = tk.Entry(self.master, width=40)
        self.input_entry.grid(row=2, column=1, padx=(0, 10))

        self.send_button = tk.Button(self.master, text="Send", command=self.process_input)
        self.send_button.grid(row=3, column=0, columnspan=2, pady=(10, 20))

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.grid(row=4, column=0, columnspan=2)

        self.calculator_robot()

    def process_input(self):
        user_input = self.input_entry.get().strip()
        self.input_entry.delete(0, tk.END)
        self.result_text.insert(tk.END, f"\nYou: {user_input}\n", "user")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            self.result_text.insert(tk.END, "Venix: Goodbye! If you have more questions, feel free to ask.\n", "venix")
        else:
            try:
                self.result_text.insert(tk.END, "Venix: I'm on it! Get ready for the result! 🚀\n", "venix")
                result = eval(user_input)
                self.result_text.insert(tk.END, f"Venix: The result is {result}\n", "venix")
            except Exception as e:
                self.result_text.insert(tk.END, f"Venix: Oops! There seems to be an error. {str(e)}\n", "venix")

    def calculator_robot(self):
        current_year = datetime.datetime.now().year
        welcome_message = f"Venix: Hello! I'm Venix, your calculator bot. Let's chat about numbers!\nVenix: I was created in {current_year}.\nVenix: You can exit at any time by typing 'exit', 'quit', or 'bye'.\n"
        self.result_text.insert(tk.END, welcome_message, "venix")

def main():
    root = tk.Tk()
    calculator_bot = CalculatorRobot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
