# Simple-Calculator

## Aim

To develop a simple calculator application in Python that performs basic arithmetic operations (addition, subtraction, multiplication and division) on two numbers.

## Description

This is a command-line calculator. The program shows a menu, asks the user to choose an operation, takes two numbers as input and displays the result. It also handles invalid input (such as text instead of a number) and division by zero.

The program has four functions, one for each operation:

- `add(a, b)` returns the sum of two numbers
- `sub(a, b)` returns the difference of two numbers
- `mul(a, b)` returns the product of two numbers
- `div(a, b)` returns the quotient of two numbers

## Main Function

The main part of the program runs in a loop:

1. Display the menu once.
2. Ask the user for a choice (`1`, `2`, `3`, `4` or `q`).
3. Read the first and second numbers.
4. Call the matching function (`add`, `sub`, `mul` or `div`).
5. Print the result and ask for the next choice, until the user enters `q`.

## Input

| Input | Description |
|-------|-------------|
| Choice | `1` Addition, `2` Subtraction, `3` Multiplication, `4` Division, `q` to quit |
| First number | Any number |
| Second number | Any number (cannot be `0` for division) |

## Output

<img width="1471" height="823" alt="Screenshot 2026-10-27 164304" src="https://github.com/user-attachments/assets/479ddc18-3463-48a3-a58c-0e0b309ec0b1" />


 <img width="1379" height="805" alt="Screenshot 2026-10-27 164312" src="https://github.com/user-attachments/assets/4c9ba880-771c-48c1-b7e0-50ff881c870c" />



 

For wrong input, the following messages are shown:

```
Error: Invalid numeric input.
Error: Cannot divide by zero.
```

## Sample Run

```
=== Simple Calculator ===
Select an operation (1/2/3/4) or 'q' to quit:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice: 1
Enter first number: 15
Enter second number: 25
Result: 15 + 25 = 40
```

## Try It Yourself

If you wish to try this program, run the following command:

```
python calculator.py
``` 
