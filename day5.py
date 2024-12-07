with open('input.txt', 'r') as f:
    input = f.readlines()

rules = []
updates = []

for line in input:
    line = line.strip()
    if '|' in line:
        s = line.split('|')
        rules.append((int(s[0]), int(s[1])))
    elif ',' in line:
        updates.append([int(page) for page in line.split(',')])

def is_update_correct(update):
    for rule in rules:
        if (rule[0] in update) and (rule[1] in update):
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

def get_middle_value(update):
    return update[int(0.5*len(update))]

print(sum([get_middle_value(update) for update in updates if is_update_correct(update)]))

def reorder(update, attempt_count=0):
    if attempt_count >= 100:
        print(f"Stopping after {attempt_count} attempts to correct {update}")
        return None
    for rule in rules:
        if (rule[0] in update) and (rule[1] in update):
            i0 = update.index(rule[0])
            i1 = update.index(rule[1])
            if i0 > i1:
                update[i0], update[i1] = update[i1], update[i0]
    if not is_update_correct(update):
        update = reorder(update, attempt_count=attempt_count+1)
    return update

print(sum([get_middle_value(reorder(update)) for update in updates if not is_update_correct(update)]))