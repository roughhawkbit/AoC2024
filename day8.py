with open('input.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

map_depth = len(input)
map_width = len(input[0])

def is_valid_position(position):
    return (0 <= position[0] < map_depth) and (0 <= position[1] < map_width)

antennae_maps = {}
for i, line in enumerate(input):
    for j, char in enumerate(line):
        if char == '.':
            continue
        position = (i,j)
        if char in antennae_maps:
            antennae_maps[char].append(position)
        else:
            antennae_maps[char] = [position]

antinodes = []

for type, map in antennae_maps.items():
    n_antennae = len(map)
    for i in range(n_antennae - 1):
        for j in range(i+1, n_antennae):
            diff_0 = map[i][0]-map[j][0]
            diff_1 = map[i][1]-map[j][1]
            # multiplier = 1
            for multiplier in range(max(map_depth, map_width)):
                potential_antinode = (
                    map[i][0]+multiplier*diff_0,
                    map[i][1]+multiplier*diff_1
                )
                if is_valid_position(potential_antinode):
                    antinodes.append(potential_antinode)
                else:
                    break
            for multiplier in range(max(map_depth, map_width)):
                potential_antinode = (
                    map[j][0]-multiplier*diff_0,
                    map[j][1]-multiplier*diff_1
                )
                if is_valid_position(potential_antinode):
                    antinodes.append(potential_antinode)
                else:
                    break

print(len(set(antinodes)))