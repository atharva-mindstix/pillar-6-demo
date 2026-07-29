"""
Calculator Backend
A simple calculator backend with core arithmetic operations.
"""

class Calculator:
    """Calculator backend class with basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.result = 0
        self.history = []
    
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, a, b):
        """Raise a to the power of b."""
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    def square_root(self, a):
        """Calculate square root of a."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = a ** 0.5
        self.history.append(f"√{a} = {result}")
        return result
    
    def percentage(self, a, b):
        """Calculate a% of b."""
        result = (a / 100) * b
        self.history.append(f"{a}% of {b} = {result}")
        return result
    
    def clear_history(self):
        """Clear calculation history."""
        self.history = []
    
    def get_history(self):
        """Get calculation history."""
        return self.history


if __name__ == "__main__":
    # Test the calculator
    calc = Calculator()
    print("Calculator Backend Test")
    print("=" * 40)
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    print(f"10 ÷ 5 = {calc.divide(10, 5)}")
    print(f"2 ^ 3 = {calc.power(2, 3)}")
    print(f"√16 = {calc.square_root(16)}")
    print(f"20% of 100 = {calc.percentage(20, 100)}")
    print("\nHistory:")
    for item in calc.get_history():
        print(f"  {item}")
