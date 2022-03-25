"""
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val):
        self.stack.append(val)
        self.size += 1
        return self.stack

    def pop(self):
        self.stack.pop()
        self.size -= 1
        return self.stack

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)


MinStack = MinStack()
MinStack.push(-2)
MinStack.push(0)
MinStack.push(-3)
MinStack.getMin()
MinStack.pop()
MinStack.top()
MinStack.getMin()
