def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def get_number(prompt, check_zero=False):
    while True:
        try:
            num = float(input(prompt))
        except ValueError:
            print("Error: Invalid numeric input.")
            continue
        if check_zero and num == 0:
            print("Error: Cannot divide by zero.")
            continue
        return num


print("=== Simple Calculator ===")
print("Select an operation (1/2/3/4) or 'q' to quit:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice: ")

    if choice == "q":
        break

    if choice not in ("1", "2", "3", "4"):
        print("Error: Invalid choice.")
        continue

    n1 = get_number("Enter first number: ")
    n2 = get_number("Enter second number: ", check_zero=(choice == "4"))

    if choice == "1":
        print(f"Result: {n1:g} + {n2:g} = {add(n1, n2):g}")
    elif choice == "2":
        print(f"Result: {n1:g} - {n2:g} = {sub(n1, n2):g}")
    elif choice == "3":
        print(f"Result: {n1:g} * {n2:g} = {mul(n1, n2):g}")
    else:
        print(f"Result: {n1:g} / {n2:g} = {div(n1, n2):g}")
