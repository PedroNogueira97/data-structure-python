import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Stack:
    def __init__(self):
        self.count = 0
        self.items = {}

    def push(self, item):
        self.items[self.count] = item
        self.count += 1
    
    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def pop(self):
        if self.is_empty():
            return None
        self.count -= 1
        result = self.items[self.count]
        del self.items[self.count]
        return result

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.count - 1]
    
    def clear(self):
        self.items = {}
        self.count = 0
    
    def return_stack(self):
        stack = [x for x in self.items.values()]
        return stack

    
        
        