with open('input.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

lab_depth = len(input)
lab_width = len(input[0])

if not len(set([len(row) for row in input])) == 1:
    print('Rows are not all the same width!')

orientations = {
    '^': (-1, 0),
    '>': (0, +1),
    'v': (+1, 0),
    '<': (0, -1)
}

obstructions = []

for i in range(lab_depth):
    for j in range(lab_width):
        if input[i][j] == '#':
            obstructions.append((i,j))
        elif input[i][j] in orientations.keys():
            starting_guard_position = [i,j,input[i][j]]

def is_in_lab(position):
    return (0 <= position[0] < lab_depth) and (0 <= position[1] < lab_width)

def get_next_orientation(orientiation):
    orientations_list = list(orientations.keys())
    if orientiation == orientations_list[-1]:
        return orientations_list[0]
    index = orientations_list.index(orientiation)
    return orientations_list[index+1]

PATROLLING = 'Patrolling'
EXITED = 'Exited'
LOOPING = 'Looping'

class Guard:
    def __init__(self, starting_position, obstructions):
        self.route = [starting_position]
        self.obstructions = obstructions
        self.status = PATROLLING
    def take_next_step(self):
        current_position = self.route[-1]
        two_forward = (
            current_position[0] + 2*orientations[current_position[2]][0], 
            current_position[1] + 2*orientations[current_position[2]][1]
        )
        next_step = (
            current_position[0] + orientations[current_position[2]][0], 
            current_position[1] + orientations[current_position[2]][1],
            get_next_orientation(current_position[2]) if two_forward in self.obstructions else current_position[2]
        )
        if not is_in_lab(next_step):
            self.status = EXITED
        elif next_step in self.route:
            self.status = LOOPING
        else:
            self.route.append(next_step)
    def locations_visited(self):
        return [(p[0],p[1]) for p in self.route]

guard = Guard(starting_guard_position, obstructions)

while guard.status == PATROLLING:
    guard.take_next_step()

print(len(guard.locations_visited()))

# Part 2 (currently doesn't quite work!)

potential_obstructions = list(set([(p[0],p[1]) for p in guard.route[2:]]))

loop_count = 0
update_freq = int(0.1*len(potential_obstructions))

for i, potential_obstruction in enumerate(potential_obstructions):
    ghost_obstructions = obstructions.copy() + [potential_obstruction]
    ghost_guard = Guard(starting_guard_position, ghost_obstructions)
    while ghost_guard.status == PATROLLING:
        ghost_guard.take_next_step()
    if ghost_guard.status == LOOPING:
        loop_count += 1
    if i % update_freq == 0:
        print(f'{i} of {len(potential_obstructions)} checked')

print(loop_count)
