for c in "abcdefg":
    print("c = ", c, end=" / ")
print()

iterator = iter("abcdefg")
for i in iterator:
    print("iterator = ", i, end=" / ")
print()

iterator = enumerate("abcdefg")
for i, j in iterator:
    print("iterator = ", i, j)