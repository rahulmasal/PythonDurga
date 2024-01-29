# all fundamental data types are immutable
# int float bool complex str
x = 10
print(id(x))
x = x + 1
print(id(x))
y = x
print(id(y))
y = y + 1
print(id(y))


a = True
b = False
print(a is b)


y = "durgasoft"
z = "durgasoft"
print(y is z)


j = 10 + 20j
k = 10 + 20j
print(id(j), id(k))
print(j is k)


# lists are mutable we can perform operation on same
# we can store multiple items of different data types in list


l = [10, 20, 30]
print(id(l))
print(l)
l[0] = 112
print(id(l))
print(l)

l2 = l
print(id(l2))
l2[1] = 0
print(l)
print(l2)
