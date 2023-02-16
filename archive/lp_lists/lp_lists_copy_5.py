''' Slices are Shallow Copies '''

# import copy
a = [[1, 2], 'b', 'c']
b = a[:]
# b = copy.deepcopy(a[:])

print(a)
print(b)

b[0][0]= 'd'

print(a)
print(b)