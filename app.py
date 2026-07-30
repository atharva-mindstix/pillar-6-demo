#!/usr/bin/env python3
"""
Simple Calculator Program
Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Main calculator interface."""
    print("Simple Calculator")
    print("=" * 40)
    print("Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Exit")
    print("=" * 40)
    
    while True:
        try:
            choice = input("\nSelect operation (1-5): ").strip()
            
            if choice == '5':
                print("Goodbye!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select 1-5.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()
