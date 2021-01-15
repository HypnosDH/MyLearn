lst = [2,9,6,3,5,8,4,7]
print(sorted(lst, key=lambda x : x if x%2==0 else x*100))
