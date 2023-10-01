class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if self.is_empty():
            print("the queue is empty ")
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0



q=Queue()
print(q.is_empty())
q.insert(3)
print(q.is_empty())
q.pop()
print(q.is_empty())
