items : [str] = []
while True:
    instr := input("Enter a string (ENTER terminates): ")
    if instr == '':
        break
    items.append(instr)

items.sort()

print("Sorted:")
for item in items:
    print(item)
