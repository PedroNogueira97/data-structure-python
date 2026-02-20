from deque import Deque

def menu():
    print("1 - Add front")
    print("2 - Add back")
    print("3 - Remove front")
    print("4 - Remove back")
    print("5 - Peek front")
    print("6 - Peek back")
    print("7 - Size")
    print("8 - Is Empty")
    print("9 - Clear")
    print("10 - Return Deque")
    print("11 - Exit")

    option = int(input("Enter your option: "))
    return option

deque = Deque()

while True:
    option = menu()
    if option == 1:
        item = input("Enter the item: ")
        deque.add_front(item)
    elif option == 2:
        item = input("Enter the item: ")
        deque.enqueue(item)
    elif option == 3:
        item = deque.dequeue()
        if item is not None:
            print("Item removed: ", item)
    elif option == 4:
        item = deque.remove_back()
        if item is not None:
            print("Item removed: ", item)
    elif option == 5:
        item = deque.peek()
        if item is not None:
            print("Item at the front: ", item)
    elif option == 6:
        item = deque.peek_back()
        if item is not None:
            print("Item at the rear: ", item)
    elif option == 7:
        print("Size of the deque: ", deque.size())
    elif option == 8:
        print("Is the deque empty? ", deque.is_empty())
    elif option == 9:
        deque.clear()
        print("Deque cleared")
    elif option == 10:
        print("Deque: ", deque.return_queue())
    elif option == 11:
        break
    else:
        print("Invalid option")
