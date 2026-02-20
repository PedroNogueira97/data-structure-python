from filas import Queue

def menu():
    print("1 - Enqueue")
    print("2 - Dequeue")
    print("3 - Peek")
    print("4 - Size")
    print("5 - Is Empty")
    print("6 - Clear")
    print("7 - Return Queue")
    print("8 - Exit")

    option = int(input("Enter your option: "))
    return option

queue = Queue()

while True:
    option = menu()
    if option == 1:
        item = input("Enter the item: ")
        queue.enqueue(item)
    elif option == 2:
        item = queue.dequeue()
        if item is not None:
            print("Item removed: ", item)
    elif option == 3:
        item = queue.peek()
        if item is not None:
            print("Item at the front: ", item)
    elif option == 4:
        print("Size of the queue: ", queue.size())
    elif option == 5:
        print("Is the queue empty? ", queue.is_empty())
    elif option == 6:
        queue.clear()
        print("Queue cleared")
    elif option == 7:
        print("Queue: ", queue.return_queue())
    elif option == 8:
        break
    else:
        print("Invalid option")