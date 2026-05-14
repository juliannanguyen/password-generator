from tkinter import *
import random
import string


class GeneratePassword:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x420")
        self.passwrd = StringVar()
        self.passlen = IntVar()
        self.passlen.set(0)

        self.lower_var = IntVar()
        self.upper_var = IntVar()
        self.digits_var = IntVar()
        self.special_var = IntVar()
        self.symbols_var = IntVar()
        self.specificChar_var = IntVar()

        self.createWidgets()
    
    def generate(self):  # Function to generate the password
        pass1 = ''
        if self.lower_var.get():
            pass1 += string.ascii_lowercase
        if self.upper_var.get():
            pass1 += string.ascii_uppercase
        if self.digits_var.get():
            pass1 += string.digits
        if self.special_var.get():
            pass1 += '★✩♡♥❆☾✧✦❋❀✿'
        if self.symbols_var.get():
            pass1 += '!@#$%^&*(~`)<>?|'
        pass2 = ''
        if self.specificChar_var.get():
            specific_chars = list(self.entry_specificChar.get())
            specific_chars = [char for char in specific_chars if char != ' ']
            random.shuffle(specific_chars)
            pass2 = ''.join(specific_chars)
            
        if self.passlen.get() == 0:
            self.passwrd.set("Password length cannot be 0.")
        elif self.passlen.get() < 0:
            self.passwrd.set("Password cannot be less than 0")
        elif len(pass2) > self.passlen.get():
            self.passwrd.set("Characters cannot exceed password length.")
        else:
            password = list(random.choice(pass1) for _ in range(self.passlen.get() - len(pass2)))

            # Concatenate the shuffled specific characters
            password += pass2

            # Shuffle the entire password
            random.shuffle(password)

            password = ''.join(password)
            self.passwrd.set(password)

    def createWidgets(self):
        # Labels
        Label(self.root, text="Password Generator", font="Arial 30 bold").pack()
        Label(self.root, text="Enter the length").pack(pady=3)
        Entry(self.root, textvariable=self.passlen).pack(pady=3)

        # Checkbuttons
        Checkbutton(self.root, text="Lowercase", variable=self.lower_var).pack()
        Checkbutton(self.root, text="Uppercase", variable=self.upper_var).pack()
        Checkbutton(self.root, text="Digits", variable=self.digits_var).pack()
        Checkbutton(self.root, text="Special Characters", variable=self.special_var).pack()
        Checkbutton(self.root, text="Symbols", variable=self.symbols_var).pack()
        Checkbutton(self.root, text="Specific Characters", variable=self.specificChar_var).pack()



        Label(self.root, text="Enter Characters:").pack()
        self.entry_specificChar = Entry(self.root)
        self.entry_specificChar.pack()

        # Buttons
        Button(self.root, text="Generate Password", command=self.generate).pack(pady=7)
        Entry(self.root, textvariable=self.passwrd).pack(pady=3)

def main():
    root = Tk()
    app = GeneratePassword(root)
    root.mainloop()

if __name__ == "__main__":
    main()
