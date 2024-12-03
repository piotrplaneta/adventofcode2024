import re

input = ""
with open("input/day03") as f:
    for l in f:
        input += l.strip()


matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)

sum = 0
for mult in matches:
    operands = re.findall(r"\d{1,3}", mult)
    sum += int(operands[0]) * int(operands[1])

print(sum)

dos = []
for m in re.finditer(r"do\(\)", input):
    dos.append(m.start())

donts = []
for m in re.finditer(r"don\'t\(\)", input):
    donts.append(m.start())

sum = 0
for mult in re.finditer(r"mul\(\d{1,3},\d{1,3}\)", input):
    mult_start = mult.start()
    matching_dos = [do_index for do_index in dos if do_index < mult_start]
    previous_do = max(matching_dos) if len(matching_dos) > 0 else -1

    matching_donts = [dont_index for dont_index in donts if dont_index < mult_start]
    previous_dont = max(matching_donts) if len(matching_donts) > 0 else -2

    if previous_do > previous_dont:
        operands = re.findall(r"\d{1,3}", input[mult.start() : mult.end()])
        sum += int(operands[0]) * int(operands[1])


print(sum)
