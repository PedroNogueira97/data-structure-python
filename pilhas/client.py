from stack import Stack

stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")

print(stack.return_stack())

stack.pop()
print(stack.return_stack())

print(stack.peek())
print(stack.size())
print(stack.is_empty())

stack.clear()
print(stack.return_stack())
print(stack.is_empty())
