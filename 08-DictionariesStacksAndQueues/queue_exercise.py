queue = []

def push(num):
    queue.append(num)

def pop(index):
    queue.pop(index)

def empty():
    for x in range(len(queue)-1,-1,-1):
        queue.pop(x)

def display():
    for x in range(len(queue)-1,-1,-1):
        print(queue[x])

push(4)
push(7)
push(12)
display()
empty()
display()
push(21)
push(14)
pop(1)
display()