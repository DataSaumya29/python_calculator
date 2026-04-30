# Simple Calculator using Python
# Author: Your Name
# Features: Add, Subtract, Multiply, Divide, Power
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
       return "cannot divide by 0"
    return a/b
def power(a,b):
    return a**b

def show_menu():
    print("\n Select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("6. Power")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "5":
        print("Calculator closed")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
        print("Result: ", add(a,b))
    elif choice =="2":
        print("Result: ", subtract(a,b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    elif choice == "6":
        print("Result:", power(a,b))
    else:
        print("Invalid choice")
    
