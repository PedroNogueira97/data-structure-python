import sys
import os
# Ensure the current directory and parent directory are in the path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from filas import Queue

def menu():
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Size")
    print("5. Is Empty")
    print("6. Clear")
    print("7. Return Queue")
    print("8. Exit")
    return int(input("Enter your choice: "))

queue = Queue()

while True:
    try:
        choice = menu()
        if choice == 1:
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
        elif choice == 2:
            item = queue.dequeue()
            if item is not None:
                print("Dequeued item:", item)
            else:
                print("Queue is empty")
        elif choice == 3:
            item = queue.peek()
            if item is not None:
                print("Peeked item:", item)
            else:
                print("Queue is empty")
        elif choice == 4:
            print("Size of queue:", queue.size())
        elif choice == 5:
            print("Is queue empty?", queue.is_empty())
        elif choice == 6:
            queue.clear()
            print("Queue cleared")
        elif choice == 7:
            print("Queue:", queue.return_queue())
        elif choice == 8:
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"An error occurred: {e}")