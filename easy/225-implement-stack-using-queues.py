#push to back
# queue.append(x)

#peek/pop from front
# queue.popleft()

#size
#size = len(self.queue)

#isempty?
#len(deque1) == 0

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.placeholderqueue = deque()

    def push(self, x: int) -> None:
        #Push element x to the "top of the stack"?
        #This means append to the right?

        self.queue.append(x)
        self.placeholderqueue.append(x)

    def pop(self) -> int:
        #Remove element on the top of the stack?
        #This means pop from the right?

        for i in range(len(self.queue) -1):
            self.queue.popleft()
        
        returnval = self.queue.popleft()

        for i in range(len(self.placeholderqueue) -1):
            self.push(self.placeholderqueue.popleft())
        
        self.placeholderqueue = self.queue.copy()

        return returnval

    def top(self) -> int:
        #Return element on the top of the stack?
        #This means return the rightmost element without modifying the queue

        for i in range(len(self.queue) -1):
            self.queue.popleft()
        
        returnval = self.queue.popleft()
        
        self.queue = self.placeholderqueue.copy()

        return returnval

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()