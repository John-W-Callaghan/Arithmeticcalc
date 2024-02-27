def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ["", "", "", ""]

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == '+':
            result = int(operand1) + int(operand2)
        else:
            result = int(operand1) - int(operand2)

        width = max(len(operand1), len(operand2)) + 2
        arranged_problems[0] += operand1.rjust(width)
        arranged_problems[1] += operator + operand2.rjust(width - 1)
        arranged_problems[2] += '-' * width
        arranged_problems[3] += str(result).rjust(width)

        if problem != problems[-1]:
            arranged_problems = [s.ljust(len(s) + 4) for s in arranged_problems]

    if show_answers:
        return '\n'.join(arranged_problems)
    else:
        return '\n'.join(arranged_problems[:3])
    return arranged_problems