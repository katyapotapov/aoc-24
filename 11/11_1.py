from time import sleep
with open("input_full.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

stones = [int(i) for i in ls[0].split()]

def blink(stones):
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:int(len(str(stone))/2)]))
            new_stones.append(int(str(stone)[int(len(str(stone))/2):]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

new_stones = stones
for i in range(25):
    new_stones = blink(new_stones)
print(len(new_stones))
