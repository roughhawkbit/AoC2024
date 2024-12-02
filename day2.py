def is_safe(report):
    is_ascending = (report[1] > report[0])
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if (diff > 0) != is_ascending:
            return False
        if (diff == 0) or abs(diff) > 3:
            return False
    return True

def is_safe_with_dampening(report):
    for i in range(len(report)):
        dampened_report = report.copy()
        dampened_report.pop(i)
        if is_safe(dampened_report):
            return True
    return(False)

# print(is_safe([7, 6, 4, 2, 1]))
# print(is_safe([1, 2, 7, 8, 9]))
# print(is_safe([9, 7, 6, 2, 1]))
# print(is_safe([1, 3, 2, 4, 5]))
# print(is_safe([8, 6, 4, 4, 1]))
# print(is_safe([1, 3, 6, 7, 9]))

n_safe = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        report = [int(x) for x in line.split()]
        if is_safe(report):
            n_safe += 1
        elif is_safe_with_dampening(report):
            n_safe += 1
print(n_safe)