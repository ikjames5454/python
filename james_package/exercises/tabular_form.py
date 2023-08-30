
print("N1" + "\t\t\t" + "N2" + "\t\t\t" + "N3" + "\t\t\t" + "N4" + "\t\t\t" + "N5")
print()
for r in range(1, 6):
    for a in range(1, 6):
        result = r ** a
        print(result, end="\t\t\t")
    print()
