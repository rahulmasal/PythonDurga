s = "rahul masal"
# [begin : end-1]
sub = s[0:5]

print(sub)

print(s[:])
print(s[0:])
print(s[:12])

print(s[5:1])  # Reverse giving empty
print(s[0:1000])  # index error not generating

print(s[0].upper() + s[1:])

print(s)
print(s[0:-1])
print(s[: len(s) - 1])
