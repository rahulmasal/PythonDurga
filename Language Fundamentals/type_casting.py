# TODO convert one type to another type is called casting
# int(), float(), complex(), bool(),str() casting functions

print(int(10.999))

# complex number not convert to int type
# print(int(10 + 12j))
print(int(True))

print(int(False))

print(int("123"))
# string internally contains only integral value which base 10
# print(int("10.5"))

print(float(0b1111))
print(float(123))
print(float("123.532"))
# print(float(123+123j))
print(float(True))
print(float(0o123))
print(float(0x123))


print(complex(123))
print(complex("12+12j"))
print(complex(0x1234 + 12j))
print(complex(0b111 + 12j))
print(complex(0o123 + 12j))
print(complex(12, 12))
# both arguments must not string
# print(complex(12, "12"))


print(bool(-12))
print(bool(0))
print(bool("0"))
print(bool("123"))
print(bool(0.233))
print(bool(0x0001))
print(bool(0o1))
print(bool())
print(bool(0b111))
print(bool(1 + 0j))
print(bool("True"))
print(bool("true"))
print(bool("false"))
print(bool(""))


print(str("10"))
print(str(10))
print(str(0o123))
print(str("10+20j"))
print(str("false"))
print(str(True))
print(str(False))
print(str(""))
