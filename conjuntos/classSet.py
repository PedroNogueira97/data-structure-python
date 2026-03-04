class Set:
    def __init__(self):
        self.items = {}

    def has(self, element):
        return element in self.items

    def add(self, element):
        if not self.has(element):
            self.items[element] = element
            return True
        return False
        
    def delete(self, element):
        if self.has(element):
            del self.items[element]
            return True
        return False    
    
    def size(self):
        count = 0
        for key in self.items:
            count += 1
        return count

    def values(self):
        values = []
        for key in self.items:
            values.append(key)
        return values
    
    def clear(self):
        self.items = {}