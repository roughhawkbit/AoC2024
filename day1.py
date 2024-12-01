x, y = [], []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        x1, y1 = line.split()
        x.append(int(x1))
        y.append(int(y1))

x.sort()
y.sort()

z = sum([abs(t[0] - t[1]) for t in zip(x, y)])

print(z)