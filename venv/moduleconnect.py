import mymodule

mymodule.greet("name")

a = mymodule.person1["age"]
b = mymodule.person1["country"]
print(a)
print(b)

import platform

x = platform.system()
print(platform.machine())
print(x)
print(platform.processor())

print(dir(platform))