import sys
import os
# Ensure the current directory and parent directory are in the path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DoublyLinkedList import DoublyLinkedList

def menu():
    print("\n1. Insert at")
    print("2. Remove at")
    print("3. Get element at")
    print("4. Size")
    print("5. Is empty")
    print("6. Clear")
    print("7. Return list")
    print("8. Exit")
    return int(input("Enter your choice: "))

doubly_linked_list = DoublyLinkedList()

while True:
    try:
        choice = menu()
        if choice == 1:
            element = input("Enter the element to insert: ")
            index = int(input("Enter the index to insert at: "))
            doubly_linked_list.insert_at(index, element)
        elif choice == 2:
            index = int(input("Enter the index to remove: "))
            doubly_linked_list.remove_at(index)
        elif choice == 3:
            index = int(input("Enter the index to get element at: "))
            node = doubly_linked_list.get_element_at(index)
            print("Element at index", index, ":", node.item if node else "None")
        elif choice == 4:
            print("Size of list:", doubly_linked_list.size())
        elif choice == 5:
            print("Is list empty?", doubly_linked_list.is_empty())
        elif choice == 6:
            # We need to implement clear if not in base class, or just re-init
            doubly_linked_list = DoublyLinkedList()
            print("List cleared")
        elif choice == 7:
            print("List:", doubly_linked_list.return_list())
        elif choice == 8:
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"An error occurred: {e}")