# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract two numbers
def subtract(x, y):
    return x - y

#multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    result = add(num1, num2)
    print("Result: ", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result: ", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result: ", result)
elif choice == '4':
    result = divide(num1, num2)
    print("Result: ", result)
else:
    print("Invalid input")
