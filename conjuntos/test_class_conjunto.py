from classSet import Set

# set = Set()
# set.add(1)
# set.add(2)
# set.add(3)
# print(set.has(1))
# print(set.has(2))
# print(set.has(3))
# print(set.has(4))
# print(set.size())
# print(set.values())

# setA = Set()
# setA.add(1)
# setA.add(2)
# setA.add(3)

# setB = Set()
# setB.add(3)
# setB.add(4)
# setB.add(5)
# setB.add(6)

# unionAB = setA.union(setB)
# print(unionAB.values())

# setA = Set()
# setA.add(1)
# setA.add(2)
# setA.add(3)
# setA.add(4)
# setA.add(5)
# setA.add(6)
# setA.add(7)

# setB = Set()
# setB.add(4)
# setB.add(5)

# intersectionAB = setA.intersection(setB)
# print(intersectionAB.values())

setA = Set()
setA.add(1)
setA.add(2)
setA.add(3)

setB = Set()
setB.add(2)
setB.add(3)
setB.add(4)

differenceAB = setA.difference(setB)
print(differenceAB.values())

 
