# identity operators
# membership operators

# a=10
# b=10
# print(a is b)
# print(a is not b)

l1=[10,20,30,40]
l2=[10,20,30,40]

print(l1 is l2)
print(l1 is not l2)
print(id(l1))
print(id(l2))
print(l1==l2)


s='hello learning python is very easy'
print('h' in s)
print('d' in s)

print('d' not in s)
print('python' in s)
print('Python' in s)

l=['sunny','bunny','chinny','vinny']
print('sunny' in l)
print('pinny' in l)
print('pinny' not in l)