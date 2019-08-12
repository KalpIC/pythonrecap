import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print("A")
print(x.strftime("%A"))
print("B")
print(x.strftime("%B"))
print("C")
print(x.strftime("%C"))
print("D")
print(x.strftime("%D"))
print("d")
print(x.strftime("%d"))

print(datetime.datetime(2019,5,20))