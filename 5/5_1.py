with open("input_full.txt") as f:
    ls = f.readlines()

rules = []
updates = []

rules_mode = True
for l in ls:
    if l == "\n":
        rules_mode = False
        continue

    if rules_mode:
        rules.append(l.strip().split("|"))
    else:
        updates.append(l.strip().split(","))

print(rules)
print("____")
print(updates)


def is_valid(update):
    for i, page in enumerate(update):
        for next_page in update[i + 1 :]:
            for rule in rules:
                # if wrong order
                if page == rule[1] and next_page == rule[0]:
                    return False
    return True


middle_pages = 0
for update in updates:
    if is_valid(update):
        middle_pages += int(update[int(len(update) / 2)])

print(middle_pages)
