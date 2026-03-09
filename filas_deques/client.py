from filas import Queue

queue = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.return_queue())

queue.dequeue()
print(queue.return_queue())

print(queue.peek())
print(queue.size())
print(queue.is_empty())

queue.clear()
print(queue.return_queue())
print(queue.is_empty())