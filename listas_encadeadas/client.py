from LinkedList import LinkedList

def menu():
    print("1 - Push")
    print("2 - Insert at")
    print("3 - Remove at")
    print("4 - Index of")
    print("5 - Remove")
    print("6 - Size")
    print("7 - Is Empty")
    print("8 - Get Head")
    print("9 - Return List")
    print("10 - Exit")

    option = int(input("Enter your option: "))
    return option

linked_list = LinkedList()

while True:
    option = menu()
    if option == 1:
        item = input("Enter the item: ")
        linked_list.push(item)
    elif option == 2:
        index = int(input("Enter the index: "))
        item = input("Enter the item: ")
        linked_list.insert_at(index, item)
    elif option == 3:
        index = int(input("Enter the index: "))
        item = linked_list.remove_at(index)
        if item is not None:
            print("Item removed: ", item)
    elif option == 4:
        item = input("Enter the item: ")
        index = linked_list.index_of(item)
        if index is not None:
            print("Item found at index: ", index)
    elif option == 5:
        item = input("Enter the item: ")
        item = linked_list.remove(item)
        if item is not None:
            print("Item removed: ", item)
    elif option == 6:
        print("Size of the list: ", linked_list.size())
    elif option == 7:
        print("Is the list empty? ", linked_list.is_empty())
    elif option == 8:
        item = linked_list.getHead()
        if item is not None:
            print("Head: ", item)
    elif option == 9:
        print("List: ", linked_list.return_list())
    elif option == 10:
        break
    else:
        print("Invalid option")
