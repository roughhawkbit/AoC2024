import re

# input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

with open('input.txt', 'r') as f:
    input = f.readlines()
input = ''.join(input)

def calc_mul_total(text):
    matches = re.findall('mul\([0-9]{1,3}\,[0-9]{1,3}\)', text)
    pairs = [s[4:-1].split(',') for s in matches]
    total = sum([int(p[0])*int(p[1]) for p in pairs])
    return(total)

print(calc_mul_total(input))

dont_splits = input.split("don't()")
total = calc_mul_total(dont_splits[0])
for s in dont_splits[1:]:
    do_splits = s.split("do()")
    for ss in do_splits[1:]:
        total += calc_mul_total(ss)

print(total)