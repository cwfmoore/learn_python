''' Shallow Copy '''

a = ['a', 'b', 'c']
b = a.copy()

# print(a, id(a))
# print(b, id(b))

b[0]= 'd'

print(a)
print(b)

