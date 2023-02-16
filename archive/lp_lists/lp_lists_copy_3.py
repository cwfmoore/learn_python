''' Shallow Copy '''

a = [[1, 2], 'b', 'c']
b = a.copy()

# print(a[0], id(a[0]))
# print(b[0], id(b[0]))

# b[0] = 'd'
b[0][0] = 'd'

print(a[0])
print(b[0])

