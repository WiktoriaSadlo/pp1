def f(n):
    if n == n[::-1]:
        return True
    return False

print(f('radar'))
print(f('12-11-21'))
print(f('book'))