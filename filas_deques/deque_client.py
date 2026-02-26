import sys
import os
# Ensure the current directory and parent directory are in the path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from deque import Deque

def menu():
    print("\n1. Add Front")
    print("2. Add Back")
    print("3. Remove Front")
    print("4. Remove Back")
    print("5. Peek Front")
    print("6. Peek Back")
    print("7. Size")
    print("8. Is Empty")
    print("9. Clear")
    print("10. Return Deque")
    print("11. Exit")
    return int(input("Enter your choice: "))

deque = Deque()

while True:
    try:
        choice = menu()
        if choice == 1:
            item = input("Enter the item to add front: ")
            deque.add_front(item)
        elif choice == 2:
            item = input("Enter the item to add back: ")
            deque.add_back(item)
        elif choice == 3:
            item = deque.remove_front()
            if item is not None:
                print("Removed front item:", item)
            else:
                print("Deque is empty")
        elif choice == 4:
            item = deque.remove_back()
            if item is not None:
                print("Removed back item:", item)
            else:
                print("Deque is empty")
        elif choice == 5:
            item = deque.peek_front()
            if item is not None:
                print("Peeked front item:", item)
            else:
                print("Deque is empty")
        elif choice == 6:
            item = deque.peek_back()
            if item is not None:
                print("Peeked back item:", item)
            else:
                print("Deque is empty")
        elif choice == 7:
            print("Size of deque:", deque.size())
        elif choice == 8:
            print("Is deque empty?", deque.is_empty())
        elif choice == 9:
            deque.clear()
            print("Deque cleared")
        elif choice == 10:
            print("Deque:", deque.return_deque())
        elif choice == 11:
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"An error occurred: {e}")
