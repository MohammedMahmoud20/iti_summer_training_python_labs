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

class InheritedQueue(Queue):
    queue_numbers = {}

    @classmethod
    def save(cls, filename):
        with open(filename, 'w') as file:
            for queue in cls.queue_numbers.values():
                file.write(f"{queue.name},{queue.size}")
                for value in queue.queue:
                    file.write(f",{value}")
                file.write("\n")

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            cls.queue_numbers = {}
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                size = int(data[1])
                queue = InheritedQueue(name, size)
                for value in data[2:]:
                    queue.insert(int(value))

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        self.queue_numbers[name] = self

    def insert(self, value):
        if len(self.queue) >= self.size:
            raise QueueOutOfRangeException("Queue is full")
        super().insert(value)

class QueueOutOfRangeException(Exception):
    pass


q1 = InheritedQueue('first_queue', 4)
q1.insert(5)
q1.insert(7)
q1.insert(3)

q2 = InheritedQueue('second_queue', 3)
q2.insert(2)
q2.insert(6)

InheritedQueue.save('queue_data.txt')
InheritedQueue.load('queue_data.txt')

for queue in InheritedQueue.queue_numbers.values():
    print(f"{queue.name}: {queue.queue}")
