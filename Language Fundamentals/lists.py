# collections related data types
# list , tuple, set, dict,range,bytes,bytearray,frozenset


# order matter ,duplicates are allowed in list

# square bracket is used in list []
# () brackets is used in tuple
# {} brackets is used in set
#  {} key value is used in dict
l = [1, 2, 3, "Durga", 5]

print(type(l))
print(l)
print(l[0])
print(l[-1])
print(l[0:])
print(l[:])
print(l[0:-1])

l.append(6)
print(l)
print(l.pop())
l.remove("Durga")
print(l)
# lists is mutable means we can change the value of specific index
l[0] = 100
print(l)
