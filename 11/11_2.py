from time import sleep
with open("input_full.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

stones = [int(i) for i in ls[0].split()]

# from functools import lru_cache
# 
# @lru_cache
def blink(num_blinks, stones):
        
    if num_blinks <= 0:
        return len(stones)

    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:int(len(str(stone))/2)]))
            new_stones.append(int(str(stone)[int(len(str(stone))/2):]))
        else:
            new_stones.append(stone * 2024)

    num_blinks -= 1
    sum_stones = 0
    if len(stones) > 300000:
        for stone in set(new_stones):
            sum_stones += blink(num_blinks, [stone]) * new_stones.count(stone) 
        return sum_stones
    else:
        return blink(num_blinks, new_stones)

print(blink(75, stones))

