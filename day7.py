with open('input.txt', 'r') as f:
    input = f.readlines()

class Equation:
    def __init__(self, line):
        ls = line.split(': ')
        self.test_value = int(ls[0])
        self.numbers = [int(n) for n in ls[1].split()]
    def can_solve(self, operators):
        list_of_trial_operators = [[o] for o in operators]
        results = [self._try_solution(trial_operators, operators) for trial_operators in list_of_trial_operators]
        return any(results)
    def _try_solution(self, trial_operators, operators):
        tally = self.numbers[0]
        for i, operator in enumerate(trial_operators):
            if operator == '+':
                tally += self.numbers[i+1]
            elif operator == '*':
                tally = tally * self.numbers[i+1]
            elif operator == '||':
                tally = int(str(tally) + str(self.numbers[i+1]))
        if tally > self.test_value:
            return False
        if len(trial_operators)< len(self.numbers) - 1:
            list_of_trial_operators = [trial_operators.copy() + [o] for o in operators]
            results = [self._try_solution(trial_operators, operators) for trial_operators in list_of_trial_operators]
            return any(results)
        else:
            return tally == self.test_value

equations = [Equation(line) for line in input]

print(sum([equation.test_value for equation in equations if equation.can_solve(['+', '*'])]))

print(sum([equation.test_value for equation in equations if equation.can_solve(['+', '*', '||'])]))