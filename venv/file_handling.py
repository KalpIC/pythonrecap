import os

for x in range(10):
    print("# ",end=" ")
    if x==9:
        print("\n") # can use simply print()

f = open("demofile.txt","r")
print(f.read())
f.close()

f1 = open("demofile1.txt")
print(f1.read(5)) # read first five character
f1.close()

f = open("demofile.txt","r")
print(f.readline())
print(f.readline())
f.close()



f1 = open("demofile1.txt")
for x in f1:
    print(x)
f1.close()

# f = open("demofile.txt", "a")
# f.write("new content from python")
# f.close()

f = open("demofile.txt","r")
print(f.read())
f.close()

f1 = open("demofile1.txt", "w")
f1.write("your content was erased with w, new content is nothing")
f1.close()

print("last f1 code")

f1 = open("demofile1.txt","r")
print(f1.read())
f1.close
print("code finish here")
print("code finish here")

f3 = open("demofile3.txt","w")
f3.write("this file will be deleted by os remove command")
f3.close

f3 = open("demofile3.txt","r")
print(f3.read())
f3.close

# if os.path.exists("demofile3.txt"):
#     os.remove("demofile3.txt")
# else:
#     print("1 2 3 file does not exist")
# os.remove("demofile3,txt")