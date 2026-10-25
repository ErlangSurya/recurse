def cracklepop(n):
    output = ""
    if n % 3 == 0:
        output += "Crackle"
    if n % 5 == 0:
        output += "Pop"
    return output if output != "" else n

for i in range(1,101):
    print(cracklepop(i))