print("Printing Patterns")

for i in range(4):
    for j in range(4):
        print("# ",end="")

    print()

for i in range(4):
    for j in range(i):
        print("# ",end="")

    print()

for i in range(0,20,2):
    for j in range(i):
        print("* ",end ="")

    print()

for i in range(4):
    for j in range(4-i):
        print("# ",end="")

    print()