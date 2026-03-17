from stack import Stack

def check_palindrome(word):
    stack = Stack()
    for letter in word.lower():
        stack.push(letter)
    
    reversed_word = ""
    while not stack.is_empty():
        reversed_word += stack.pop()
    
    palindrome = word.lower() == reversed_word
    return f"The word {word} is {'a' if palindrome else 'not a'} palindrome"

print(check_palindrome("Ana"))
print(check_palindrome("hello"))
