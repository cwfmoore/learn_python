''' Copies and References '''

a = ['a', 'b', 'c']
b = a.copy()

# print(a, id(a))
# print(b, id(b))

a[0]= 'd'

print(a)
print(b)

