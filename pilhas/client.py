from stack import Stack

def menu():
    print("1. Push")
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
    choice = menu()
    if choice == 1:
        item = int(input("Enter the item to push: "))
        stack.push(item)
    elif choice == 2:
        item = stack.pop()
        if item is not None:
            print("Popped item:", item)
    elif choice == 3:
        item = stack.peek()
        if item is not None:
            print("Peeked item:", item)
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