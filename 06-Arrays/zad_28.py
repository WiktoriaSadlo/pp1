def f(arr1,arr2):
    if len(arr1)==len(arr2):
        for x in range(len(arr1)):
            if arr1[x]!=arr2[x]:
                return False
        return True
    else:
        return False

#a
a1 = ['water','book','sky']
a2 = ['water','book','sky']
print(f(a1,a2))

#b
b1 = [True,False]
b2 = [True,False,True]
print(f(b1,b2))

#c
c1 = [5,3,1]
c2 = [5,3,1]
print(f(c1,c2))

#d
d1 = [3,2,1]
d2 = [3,2]
print(f(d1,d2))