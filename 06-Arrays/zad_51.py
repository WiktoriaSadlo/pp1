x = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7]]

def swap(n):
    last = n[len(n)-1]
    first = n[0]
    n.pop(0)
    n.pop(len(n)-1)
    n.insert(0,last)
    n.insert(len(n),first)
    return n

print(swap(x))