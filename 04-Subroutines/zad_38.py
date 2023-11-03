def f(n):
    n_reversed=''
    for x in range(len(n)-1,-1,-1):
        n_reversed+=n[x]
    if n == n_reversed:
        return True
    return False

print(f('radar'))
print(f('12-11-21'))
print(f('book'))