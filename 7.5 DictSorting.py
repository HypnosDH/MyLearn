d = dict(zip("abc", (3, 2, 1)))
print("Ori Dict:{}".format(d))

key_sorted = sorted(d.keys())
print("Sotted by Key:")
for k in key_sorted:
    print("{} --> {}".format( k , d[k]))

value_sorted = sorted(d.values())
print("Sotted by values:")
for v in value_sorted:
    key_list = [key for key, value in d.items() if value == v]
    print("{} --> {}".format(key_list, v))
    print("{} --> {}".format(". ".join(key_list), v))