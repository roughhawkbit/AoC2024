with open('input.txt', 'r') as f:
    input = f.readlines()

map = [[int(c) for c in line.strip()] for line in input]

trailheads = []
for i, row in enumerate(map):
    for j in range(len(row)):
        if row[j] == 0:
            trailheads.append((i,j))

neighbour_diffs = [(1,0), (-1,0), (0, 1), (0, -1)]

def is_valid_location(i, j):
    return (0 <= i < len(map)) and (0 <= j < len(map[i]))

trailhead_values = {}

for trailhead in trailheads:
    trailmap = [[None]*len(row) for row in map]
    current_locs = [trailhead]
    next_locs = []
    for hgt in range(9):
        for loc in current_locs:
            for diff in neighbour_diffs:
                nghbr_i = loc[0] + diff[0]
                nghbr_j = loc[1] + diff[1]
                if is_valid_location(nghbr_i, nghbr_j) and (map[nghbr_i][nghbr_j] == hgt + 1):
                    next_locs.append((nghbr_i, nghbr_j))
        current_locs = list(set(next_locs))
        next_locs = []
    trailhead_values[trailhead] = len(current_locs)

print(sum(trailhead_values.values()))

trailhead_values = {}

for trailhead in trailheads:
    trailmap = [[None]*len(row) for row in map]
    current_locs = [trailhead]
    next_locs = []
    for hgt in range(9):
        for loc in current_locs:
            for diff in neighbour_diffs:
                nghbr_i = loc[0] + diff[0]
                nghbr_j = loc[1] + diff[1]
                if is_valid_location(nghbr_i, nghbr_j) and (map[nghbr_i][nghbr_j] == hgt + 1):
                    next_locs.append((nghbr_i, nghbr_j))
        current_locs = next_locs
        next_locs = []
    trailhead_values[trailhead] = len(current_locs)

print(sum(trailhead_values.values()))