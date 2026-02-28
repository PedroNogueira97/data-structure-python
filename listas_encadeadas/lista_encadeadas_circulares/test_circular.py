import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CircularLinkedList import CircularLinkedList

def test_circular_list():
    circular = CircularLinkedList()
    
    print("--- Testando push (no final) ---")
    circular.push(1)
    circular.push(2)
    circular.push(3)
    print(f"Lista: {circular.return_list()}") # LinkedList.return_list() can be used but it doesn't show circularity
    
    # Manually check circularity
    head = circular.getHead()
    last = circular.get_element_at(circular.size() - 1)
    print(f"Head item: {head.item}")
    print(f"Last item next points to head? {last.next == head}")

    print("\n--- Testando insert_at(0, 0) ---")
    circular.insert_at(0, 0)
    print(f"Lista: {circular.return_list()}")
    head = circular.getHead()
    last = circular.get_element_at(circular.size() - 1)
    print(f"Head item: {head.item}")
    print(f"Last item next points to head? {last.next == head}")

    print("\n--- Testando insert_at(2, 1.5) ---")
    circular.insert_at(2, 1.5)
    print(f"Lista: {circular.return_list()}")
    
    # Final circularity check
    head = circular.getHead()
    last = circular.get_element_at(circular.size() - 1)
    print(f"Last item: {last.item}")
    print(f"Last item next points to head? {last.next == head}")

if __name__ == "__main__":
    test_circular_list()
