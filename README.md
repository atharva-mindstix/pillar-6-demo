# pillar-6-demo

A simple calculator program demonstration.

## Overview

This project implements a basic calculator program in Python that performs fundamental arithmetic operations.

## Calculator Program (app.py)

### Features

The calculator program supports the following operations:
- **Addition** (+): Add two numbers
- **Subtraction** (-): Subtract one number from another
- **Multiplication** (*): Multiply two numbers
- **Division** (/): Divide one number by another (with zero-division handling)

### Implementation Guide

#### Structure

The `app.py` file should contain:

1. **Calculator Class or Functions** - Core arithmetic operations
2. **User Interface** - Command-line interface for user interaction
3. **Input Validation** - Ensure valid numeric inputs
4. **Error Handling** - Handle edge cases (division by zero, invalid inputs)

#### Example Usage

```python
# Running the calculator
python app.py
```

**Sample interaction:**
```
Welcome to Simple Calculator!
Enter first number: 10
Enter operation (+, -, *, /): +
Enter second number: 5
Result: 15.0
```

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses standard library only)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/atharva-mindstix/pillar-6-demo.git
   cd pillar-6-demo
   ```

2. Ensure Python is installed:
   ```bash
   python --version
   ```

3. Run the calculator:
   ```bash
   python app.py
   ```

### Program Design

#### Recommended Functions

```python
def add(a, b)       # Returns a + b
def subtract(a, b)  # Returns a - b
def multiply(a, b)  # Returns a * b
def divide(a, b)    # Returns a / b (handles zero division)
```

#### Main Loop

The program should:
1. Display a welcome message
2. Prompt for first number
3. Prompt for operation (+, -, *, /)
4. Prompt for second number
5. Calculate and display result
6. Ask if user wants to continue or exit

### Error Handling

- **Invalid numeric input**: Catch `ValueError` and prompt again
- **Division by zero**: Check denominator before division
- **Invalid operation**: Validate operation is one of: +, -, *, /

### Testing

Test the calculator with:
- Positive and negative numbers
- Decimal values
- Zero as an operand
- Division by zero (should handle gracefully)
- Invalid inputs (non-numeric values)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

This project is for demonstration purposes.
