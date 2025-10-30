class Stack:
    def __init__(self,max_size):
        self.stack=[]
        self.max_size=max_size
    def push(self,item):
        if len(self.stack)>=self.max_size:
            print("stack overflow,cannot push",item)
        else:
            self.stack.append(item)
            print(f"pushed: {item}")
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            removed=self.stack.pop()
            print(f"popped: {removed}")
    def peek(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("top element",self.stack[-1])
    def display(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("stack: ",self.stack)
stack=Stack(max_size=3)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.display()

stack.peek()

stack.pop()
stack.pop()
stack.pop()
stack.pop()

