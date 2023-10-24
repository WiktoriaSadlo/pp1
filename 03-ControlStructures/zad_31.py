x = int(input('Enter x coordinate:'))
y = int(input('Enter y coordinate:'))

if x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the secound quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
elif x==0 and y!=0:
    print(f"Point P({x},{y}) is on axis x")
elif y==0 and x!=0:
    print(f"Point P({x},{y}) is on axis y")
else:
    print(f"Point P({x},{y}) is in in the position (0,0)")