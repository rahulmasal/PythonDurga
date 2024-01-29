# none means nothing no value associated
a = 19
print(type(a))

a = None

print(a)

print(type(a))


def f1():
    return 10


x = f1()

print(x)


def f2():
    print("hello")


y = f2()

print(y)
# None is only object type
print(id(a))
# None created only once in troughout program by python virtual machine

print(id(a), id(y))
