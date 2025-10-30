class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    # Enqueue
    def enqueue(self, item):
        if len(self.queue) >= self.max_size:
            print("Queue Overflow! Cannot enqueue", item)
        else:
            self.queue.append(item)
            print(f"Enqueued: {item}")

    # Dequeue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow! Cannot dequeue")
        else:
            removed = self.queue.pop(0)  # Remove from front
            print(f"Dequeued: {removed}")

    # Peek front element
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    # Display queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)

q = Queue(max_size=3)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)   

q.display()

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()     

q.peek()
