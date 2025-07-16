class Calc:
    def __init__(self):
        self.get_numbers()

    def get_numbers(self):
        while True:
            try:
                self.n1 = float(input("Enter the first number: "))
                self.n2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def perform_operation(self):
        while True:
            op = input("Specify the operation (+, -, *, /): ").strip()
            if op == '+':
                result = self.n1 + self.n2
                print("The result is:", result)
                break
            elif op == '-':
                result = self.n1 - self.n2
                print("The result is:", result)
                break
            elif op == '*':
                result = self.n1 * self.n2
                print("The result is:", result)
                break
            elif op == '/':
                if self.n2 == 0:
                    print("Error: Cannot divide by zero. Please enter numbers again.")
                    self.get_numbers()
                    continue
                result = self.n1 / self.n2
                print("The result is:", result)
                break
            else:
                print("Invalid operation. Please enter one of +, -, *, /")

    def run(self):
        self.perform_operation()

# Run the calculator
calc = Calc()
calc.run()
