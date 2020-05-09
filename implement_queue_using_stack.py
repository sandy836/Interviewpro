class Queue:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_denqueue = []
    def enqueue(self, val):
        self.stack_enqueue.append(val)
    def dequeue(self):
        if self.stack_denqueue:
            return self.stack_denqueue.pop()
        else:
            while self.stack_enqueue:
                self.stack_denqueue.append(self.stack_enqueue.pop())
            if self.stack_denqueue:
                return self.stack_denqueue.pop()
            return "Queue is Empty"
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(3)
