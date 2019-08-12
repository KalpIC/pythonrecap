nums =[12,16,18,21,20,24]

tup = (25, 58,51)
print(type(tup))

for num in nums:
    if num % 5 ==0:
        print(num)
        break
else:
    print("not found")