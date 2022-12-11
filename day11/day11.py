import itertools
import operator
import math

with open("day11.txt") as f:
    data = [line.strip() for line in f]

OPERATORS = {
    "+": operator.add,
    "*": operator.mul
}


class Monkey:
    def __init__(self, items):
        self.curr = items
        self.operation_function = None
        self.operand = None
        self.inspected = 0
        self.divisor = None
        self.manage_item = lambda num: num // 3

    def set_operation(self, operator, operand):
        self.operation_function = OPERATORS[operator]
        self.operand = operand

    def set_throwing_action(self, divisor, monkey_a, monkey_b):
        self.divisor = divisor
        self.monkey_a = monkey_a
        self.monkey_b = monkey_b

    def set_manage_item(self, manage_item):
        self.manage_item = manage_item

    def operation(self, number):
        return self.operation_function(number, number) if self.operand == None else self.operation_function(number, int(self.operand))

    def execute(self):
        while self.curr:
            item = self.curr.pop()
            item = self.operation(item)
            item = self.manage_item(item)
            if item % self.divisor == 0:
                self.monkey_a.curr.append(item)
            else:
                self.monkey_b.curr.append(item)
            self.inspected += 1


def parse_monkeys():
    monkeys_data = [list(j) for i, j in itertools.groupby(
        data, key=lambda i: i == '') if not i]
    monkeys = []
    for monkey in monkeys_data:
        starting = list(map(int, monkey[1].rsplit(": ", 1)[1].split(", ")))
        monkey = Monkey(starting)
        monkeys.append(monkey)

    for index, monkey_data in enumerate(monkeys_data):
        monkey = monkeys[index]
        _, operation, operand = monkey_data[2].rsplit(" ", 2)
        monkey.set_operation(operation, operand if operand != "old" else None)
        divisor = int(monkey_data[3].rsplit(" ")[-1])
        monkey_a_index = int(monkey_data[4].rsplit(" ")[-1])
        monkey_b_index = int(monkey_data[5].rsplit(" ")[-1])
        monkey.set_throwing_action(
            divisor, monkeys[monkey_a_index], monkeys[monkey_b_index])

    return monkeys


def use_lcm(monkeys):
    divisors = []
    for monkey in monkeys:
        divisors.append(monkey.divisor)
    lcm = math.lcm(*divisors)
    for monkey in monkeys:
        monkey.manage_item = lambda num: num % lcm


def solve(rounds, manage_with_lcm):
    monkeys = parse_monkeys()
    if manage_with_lcm:
        use_lcm(monkeys)
    for round in range(rounds):
        for monkey in monkeys:
            monkey.execute()

    monkeys.sort(key=operator.attrgetter("inspected"))
    return monkeys[-1].inspected * monkeys[-2].inspected


print("Part 1:", solve(20, False))
print("Part 2:", solve(10000, True))
