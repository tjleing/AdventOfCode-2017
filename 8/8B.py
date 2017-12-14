import sys

registers = {}

max_reg = -1
for line in sys.stdin:
    line = line.split()

    reg = line[0]
    operator = line[1]
    how_much = int(line[2])
    # line[3] is always "if"
    condition_reg = line[4]
    comparator = line[5]
    compare_value = int(line[6])

    condition_reg_value = 0
    if condition_reg in registers:
        condition_reg_value = registers[condition_reg]

    perform_operation_or_not = True
    if comparator == "==":
        perform_operation_or_not = (condition_reg_value == compare_value)
    if comparator == "!=":
        perform_operation_or_not = (condition_reg_value != compare_value)
    if comparator == "<=":
        perform_operation_or_not = (condition_reg_value <= compare_value)
    if comparator == ">=":
        perform_operation_or_not = (condition_reg_value >= compare_value)
    if comparator == "<":
        perform_operation_or_not = (condition_reg_value < compare_value)
    if comparator == ">":
        perform_operation_or_not = (condition_reg_value > compare_value)

    if perform_operation_or_not:
        if reg not in registers:
            registers[reg] = 0
        if operator == "inc":
            registers[reg] += how_much
        else:
            registers[reg] -= how_much
        max_reg = max(max_reg, registers[reg])

print(max_reg)
