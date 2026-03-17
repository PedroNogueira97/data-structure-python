import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Queue:
    def __init__(self):
        self.items = {}
        self.count = 0
        self.lowestcount = 0

    def enqueue(self, item):
        self.items[self.count] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        
        result = self.items[self.lowestcount]
        del self.items[self.lowestcount]
        self.lowestcount += 1
        return result

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.lowestcount]

    def size(self):
        return self.count - self.lowestcount

    def is_empty(self):
        return self.size() == 0

    def return_queue(self):
        return [x for x in self.items.values()]
        
    def clear(self):
        self.items = {}
        self.count = 0
        self.lowestcount = 0

