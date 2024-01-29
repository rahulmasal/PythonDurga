# to represent group of bytes values
l = [10, 20, 30, 255]

b = bytes(l)

print(b)

print(type(b))

for x in b:
    print(x)

print(b[0])
print(b[:1])
# b[0]=1
# bytes are immutable


b2 = bytearray(l)
print(b2)
for y in b2:
    print(y)

print(b2[0])
print(b2[0:2])
b2[0] = 12
for y in b2:
    print(y)
# bytes array are mutable
