import re

with open('input.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

count = 0
patterns = ['XMAS', 'SAMX']

# Horizontals
for i in range(len(input)):
    for j in range(len(input[0])-3):
        snippet = input[i][j:j+4]
        if snippet in patterns:
            count += 1

# Verticals
for i in range(len(input)-3):
    for j in range(len(input[0])):
        snippet = ''.join([line[j] for line in input[i:i+4]])
        if snippet in patterns:
            count += 1

# Diagonals
for i in range(len(input)-3):
    for j in range(len(input[0])-3):
        # NE-SW
        snippet = ''.join([input[i+k][j+k] for k in range(4)])
        if snippet in patterns:
            count += 1
        # NW-SE
        snippet = ''.join([input[i+k][j+3-k] for k in range(4)])
        if snippet in patterns:
            count += 1
        
print(count)            

count = 0
patterns = ['MS', 'SM']

for i in range(len(input)-2):
    for j in range(len(input[0])-2):
        if not input[i+1][j+1] == 'A':
            continue
        snippet = input[i][j] + input[i+2][j+2]
        if not snippet in patterns:
            continue
        snippet = input[i][j+2] + input[i+2][j]
        if not snippet in patterns:
            continue
        count += 1

print(count)