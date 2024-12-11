with open('input.txt', 'r') as f:
    input = f.readline()

stones = [int(c) for c in input.split(' ')]

print(stones)

def blink(stones):
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == 0:
            stones[i] = 1
        elif len(str(stone)) % 2 == 0:
            c = str(stone)
            l = len(c)
            stones[i] = int(c[:int(l/2)])
            new_stones.append((i, int(c[int(l/2):])))
        else:
            stones[i] = stone * 2024
    for i, new_stone in enumerate(new_stones):
        stones.insert(new_stone[0]+i+1, new_stone[1])
    return stones

for i in range(25):
    stones = blink(stones)
    # print(stones)
    # print(f"{i}: {len(stones)}")

print(len(stones))