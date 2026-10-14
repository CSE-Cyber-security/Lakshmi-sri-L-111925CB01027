 # Fibonacci Series in Python

## Aim
To write a Python program that prints the Fibonacci series for n terms.

## Description
The Fibonacci series is a sequence where each number is the sum of the
previous two numbers. It starts with 0 and 1.

How the program works:
1. It reads the number of terms `n` from the user.
2. It starts with `a = 0` and `b = 1`.
3. A loop runs `n` times. In each round it prints `a`, then updates
   the values using `a, b = b, a + b`.
4. If `n` is zero or negative, it prints a message asking for a positive number.

## How to Run
```
python fibonacci.py
```

## Input
```
7
```

## Output
```
0 1 1 2 3 5 8
```

## Files
- `fibonacci.py` - the program
- `README.md` - aim, description, input and output
