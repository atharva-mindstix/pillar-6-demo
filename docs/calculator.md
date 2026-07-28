# Simple Calculator Program

## Overview

This document describes a simple calculator program that performs basic arithmetic operations.

## Features

The calculator supports the following operations:

- **Addition (+)**: Add two numbers
- **Subtraction (-)**: Subtract one number from another
- **Multiplication (×)**: Multiply two numbers
- **Division (÷)**: Divide one number by another

## Usage Examples

### Addition
```
Input: 5 + 3
Output: 8
```

### Subtraction
```
Input: 10 - 4
Output: 6
```

### Multiplication
```
Input: 7 × 6
Output: 42
```

### Division
```
Input: 20 ÷ 5
Output: 4
```

## Implementation Guidelines

### Basic Structure

A simple calculator can be implemented with the following components:

1. **Input Handler**: Accepts user input for numbers and operations
2. **Operation Processor**: Determines which arithmetic operation to perform
3. **Calculator Engine**: Executes the mathematical operations
4. **Output Handler**: Displays the result to the user

### Error Handling

The calculator should handle common errors:

- **Division by Zero**: Display an error message when attempting to divide by zero
- **Invalid Input**: Validate that inputs are valid numbers
- **Invalid Operation**: Check that the operation is one of the supported types

### Example Pseudocode

```
function calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '×' or operator == '*':
        return num1 * num2
    elif operator == '÷' or operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"
```

## Testing

Test cases to validate the calculator:

| Test Case | Input | Expected Output |
|-----------|-------|----------------|
| TC1 | 5 + 3 | 8 |
| TC2 | 10 - 7 | 3 |
| TC3 | 4 × 5 | 20 |
| TC4 | 15 ÷ 3 | 5 |
| TC5 | 10 ÷ 0 | Error: Division by zero |
| TC6 | -5 + 8 | 3 |
| TC7 | 0 × 100 | 0 |

## Future Enhancements

Possible improvements for the calculator:

- Support for more advanced operations (power, square root, modulo)
- Memory functions (store and recall)
- History of calculations
- Support for decimal numbers
- Parentheses for order of operations
- Scientific calculator functions

## Conclusion

This simple calculator provides a foundation for basic arithmetic operations with room for expansion and enhancement based on user needs.
