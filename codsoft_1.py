import random
import string

class PasswordGenerator:
    def __init__(self):
        self.length = self.get_length()
        self.complexity = self.get_complexity()

    def get_length(self):
        while True:
            try:
                length = int(input("Enter the length of the password: "))
                if length <= 0:
                    print("Length must be greater than 0.")
                    continue
                return length
            except ValueError:
                print("Please enter a valid number.")

    def get_complexity(self):
        while True:
            complexity = input("Enter the complexity of the password (easy/medium/hard): ").lower()
            if complexity in ['easy', 'medium', 'hard']:
                return complexity
            print("Invalid input. Please choose from easy, medium, or hard.")

    def generate_password(self):
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = "!@#$%^&*()_+"

        if self.complexity == "easy":
            chars = lowercase
        elif self.complexity == "medium":
            chars = lowercase + uppercase
        else:  # hard
            chars = lowercase + uppercase + digits + symbols

        # Ensure at least one char from each type in medium and hard
        password = []

        if self.complexity == "medium":
            if self.length >= 2:
                password = [random.choice(lowercase), random.choice(uppercase)]
                password += random.choices(chars, k=self.length - 2)
            else:
                password = random.choices(chars, k=self.length)

        elif self.complexity == "hard":
            if self.length >= 4:
                password = [
                    random.choice(lowercase),
                    random.choice(uppercase),
                    random.choice(digits),
                    random.choice(symbols)
                ]
                password += random.choices(chars, k=self.length - 4)
            else:
                password = random.choices(chars, k=self.length)

        else:  # easy
            password = random.choices(chars, k=self.length)

        random.shuffle(password)
        return ''.join(password)

    def display(self):
        print("Your password is:", self.generate_password())

# Create and display password
pg = PasswordGenerator()
pg.display()
