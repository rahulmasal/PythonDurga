# exactly same as list except that it is immutable
# read only version of list is tuple
t = (10, 20, 30, 40)
print(t)
print(type(t))
print(t[0])
print(t[0:])
print(t[-1])
print(t.count(10))
# less memory taking tuples than lists and faster than lists so performance is betters
t2 = (10,)
print(type(t2))
# note above step , mandatory
