from filas import Queue

class Deque(Queue):
    def __init__(self):
        super().__init__()

    def add_front(self, item):
        if self.is_empty():
            self.enqueue(item)
        elif self.lowestcount > 0:
            self.lowestcount -= 1
            self.items[self.lowestcount] = item
        else:
            for i in range(self.count, 0, -1):
                self.items[i] = self.items[i - 1]
            self.count += 1
            self.lowestcount = 0
            self.items[0] = item

    def remove_back(self):
        if self.is_empty():
            return None
        self.count-=1
        result = self.items[self.count]
        del self.items[self.count]
        return result

    def peek_back(self):
        if self.is_empty():
            return None
        return self.items[self.count - 1]  
