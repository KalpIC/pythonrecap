class person:
    def __init__(self,name,age):
        self.name =name
        self.age = age


p1 = person("tony stark",35)

print(p1)
print(p1.name)
print(p1.age)

class class1():
    x = 25
    x1 = 26
    x2 = 37
    x3 = 3588



n = class1()

print(n.x,n.x1,n.x2,n.x3)

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " , self.name,"\nand my age is",self.age)


p1 = Person1("John", 36)
p1.myfunc()