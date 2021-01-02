dna1 = "AATCGATCTCGAATTCAC"
dna2 = "ATTCGTACTCGGATCCTC"
comp = ""

for i in range(len(dna1)):
    if dna1[i] == dna2[i]:
        comp += "|"
    else:
        comp += " "

for c in dna1:
    print(c ,end=" ")
print()
for c in comp:
    print(c ,end=" ")
print()
for c in dna2:
    print(c ,end=" ")
print()
    
