import sys
import os
# Ensure the current directory and parent directory are in the path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stack import Stack

def menu():
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Is Empty")
    print("6. Clear")
    print("7. Return Stack")
    print("8. Exit")
    return int(input("Enter your choice: "))

stack = Stack()

while True:
    try:
        choice = menu()
        if choice == 1:
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == 2:
            item = stack.pop()
            if item is not None:
                print("Popped item:", item)
            else:
                print("Stack is empty")
        elif choice == 3:
            item = stack.peek()
            if item is not None:
                print("Peeked item:", item)
            else:
                print("Stack is empty")
        elif choice == 4:
            print("Size of stack:", stack.size())
        elif choice == 5:
            print("Is stack empty?", stack.is_empty())
        elif choice == 6:
            stack.clear()
            print("Stack cleared")
        elif choice == 7:
            print("Stack:", stack.return_stack())
        elif choice == 8:
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"An error occurred: {e}")