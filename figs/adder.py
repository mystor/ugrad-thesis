total := 0
while True:
    instr := input('Enter a number (ENTER to stop): ')
    if instr == '':
        break
    num := int(instr)
    total += num

print('The total was:', total)
