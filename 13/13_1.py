from time import sleep

with open("input_full.txt") as f:
# with open("input.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

claw_machines = []
cur_claw = {}

# always positive
for i in range(len(ls)):
    line = ls[i]
    if line == "":
        claw_machines.append(cur_claw)
        cur_claw = {}
    else:
        if "A" in line:
            cur_claw["A"] = {}
            cur_claw["A"]["X"] = int(line[line.find("X")+2:line.find(",")])
            cur_claw["A"]["Y"] = int(line[line.find("Y")+2:])
        elif "B" in line:
            cur_claw["B"] = {}
            cur_claw["B"]["X"] = int(line[line.find("X")+2:line.find(",")])
            cur_claw["B"]["Y"] = int(line[line.find("Y")+2:])
        elif "Prize" in line:
            cur_claw["Prize"] = {}
            cur_claw["Prize"]["X"] = int(line[line.find("X")+2:line.find(",")])
            cur_claw["Prize"]["Y"] = int(line[line.find("Y")+2:])
#     for j in range(len(ls[0])):

claw_machines.append(cur_claw)


tokens = 0
for claw in claw_machines:
    sols = []
    for a in range(101):
        for b in range(101):
            x = a * claw["A"]["X"] + b * claw["B"]["X"] 
            y = a * claw["A"]["Y"] + b * claw["B"]["Y"]
            print(f"{x=},{y=},{claw['Prize']=}")
            if x == claw["Prize"]["X"] and y == claw["Prize"]["Y"]:
                sols.append(a * 3 + b)

    if len(sols) > 0:
        tokens += min(sols)

print(tokens)
