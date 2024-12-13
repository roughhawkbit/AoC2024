with open('input.txt', 'r') as f:
    input = f.readline()

stones = [int(c) for c in input.split(' ')]

# print(stones)

stone_freqs = {}
transitions = {}

for stone in stones:
    if stone in stone_freqs:
        stone_freqs[stone] = stone_freqs[stone] + 1
    else:
        stone_freqs[stone] = 1

for i in range(75):
    new_stone_freqs = {}
    for num, count in stone_freqs.items():
        if num in transitions:
            new_nums = transitions[num]
        else:
            if num == 0:
                new_nums = [1]
            elif len(str(num)) % 2 == 0:
                c = str(num)
                l = len(c)
                new_nums = [int(c[:int(l/2)]), int(c[int(l/2):])]
            else:
                new_nums = [num * 2024]
            transitions[num] = new_nums
        for new_num in new_nums:
            if new_num in new_stone_freqs:
                new_stone_freqs[new_num] = new_stone_freqs[new_num] + count
            else:
                new_stone_freqs[new_num] = count
    stone_freqs = new_stone_freqs

# print(stone_freqs)
print(sum(stone_freqs.values()))