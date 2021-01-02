dna1 = input("請輸入第一組鹼基對：").upper()
dna2 = input("請輸入第二組鹼基對：").upper()
comp = ""

DNA_len = min(len(dna1), len(dna2))
CheckDNA = True

for i in range(DNA_len):
    if (dna1[i] in "ACTG") and  (dna2[i] in "ACTG"):
        if dna1[i] == dna2[i]:
            comp += "|"
        else:
            comp += " " 
    else:
        CheckDNA = False

if CheckDNA:
    for c in dna1:
        print(c ,end=" ")
    print()
    for c in comp:
        print(c ,end=" ")
    print()
    for c in dna2:
        print(c ,end=" ")
    print()
    likeone = comp.count("|") / len(comp)
    print("DNA 相似度：{0:.2%}".format(likeone))
else:
    print("鹼基對 is error, must be in \"ACTG\"")
