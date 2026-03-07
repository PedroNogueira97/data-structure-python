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
        while count < len(self.items):
            count += 1
        return count

    def values(self):
        values = []
        for key in self.items:
            values.append(key)
        return values
    
    def clear(self):
        self.items = {}
    
    def union(self, otherSet):
        unionSet = Set()
        i = 0
        values = self.values()
        while i < len(values):
            unionSet.add(values[i])
            i += 1
        values = otherSet.values()
        i = 0
        while i < len(values):
            unionSet.add(values[i])
            i += 1
        return unionSet

    def intersection(self, otherSet):
        intersectionSet = Set()
        values = self.values()
        otherValues = otherSet.values()
        
        # Decide which set to iterate over (the smaller one)
        # and which set to check for existence (the larger one)
        if len(values) < len(otherValues):
            smallerValues = values
            largerSet = otherSet
        else:
            smallerValues = otherValues
            largerSet = self
            
        for value in smallerValues:
            if largerSet.has(value):
                intersectionSet.add(value)
        return intersectionSet

    def difference(self, otherSet):
        differenceSet = Set()
        for value in self.values():
            if not otherSet.has(value):
                differenceSet.add(value)
        return differenceSet
    
    def isSubset(self, otherSet):
        for value in self.values():
            if not otherSet.has(value):
                return False
        return True
        