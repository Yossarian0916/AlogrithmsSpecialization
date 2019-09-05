class Stack:
    def __init__(self, size):
        """self.top points to the most recently inserted element"""
        self.size = size
        self.stack = [None]*size
        self.top = -1

    def push(self, x):
        if self.top > self.size-1:
            return 'Overflow'
        self.top = self.top + 1
        self.stack[self.top] = x

    def pop(self):
        if self.is_empty():
            return 'Underflow'
        else:
            self.top = self.top - 1
            return self.stack[self.top+1]

    def is_empty(self):
        if self.top < 0:
            return True
        return False

    def __len__(self):
        return self.top


if __name__ == "__main__":
    stack = Stack(size=3)
    print(stack.is_empty())
    stack.push(15)
    stack.push('string')
    print(stack.pop())
    stack.push(0.999)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
