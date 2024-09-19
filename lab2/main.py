def operator_precedence(op1, op2):
    precedence = {'!': 3, '*': 2, '+': 1, '(': 0}
    return precedence[op2] <= precedence[op1]


def infix_to_postfix(expression):
    result = []
    stack = []
    for symbol in expression:
        if symbol.isalpha():
            result.append(symbol)
        elif symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        elif symbol in '+*!':
            while stack and stack[-1] != '(' and operator_precedence(stack[-1], symbol):
                result.append(stack.pop())
            stack.append(symbol)
    while stack:
        result.append(stack.pop())
    return result


def evaluate_postfix(expression, var_dict):
    stack = []
    for symbol in expression:
        if symbol.isalpha():
            stack.append(bool(var_dict[symbol]))
        elif symbol == '!':
            stack.append(not stack.pop())
        elif symbol == '+':
            stack.append(stack.pop() or stack.pop())
        elif symbol == '*':
            stack.append(stack.pop() and stack.pop())
    return str(int(stack[0]))


def generate_truth_table(postfix_expr):
    variables = sorted(set(filter(str.isalpha, postfix_expr)))
    table = []
    for i in range(2 ** len(variables)):
        row = format(i, '0' + str(len(variables)) + 'b')
        var_dict = {var: int(row[idx]) for idx, var in enumerate(variables)}
        result = evaluate_postfix(postfix_expr, var_dict)
        table.append(list(row) + [result])
    return variables, table


def sknf_from_truth_table(truth_table, variables):
    sknf = []
    for row in truth_table:
        if row[-1] == '0':
            sknf.append('(' + ''.join(['!' + variables[i] if bit == '1' else variables[i] for i, bit in enumerate(row[:-1])]) + ')')
    return ' + '.join(sknf)


def sdnf_from_truth_table(truth_table, variables):
    sdnf = []
    for row in truth_table:
        if row[-1] == '1':
            sdnf.append('(' + ''.join([variables[i] if bit == '1' else '!' + variables[i] for i, bit in enumerate(row[:-1])]) + ')')
    return ' * '.join(sdnf)


def index_from_truth_table(truth_table):
    return int(''.join(['1' if row[-1] == '1' else '0' for row in truth_table]), 2)


logical_expression = "!((a+b)*!(!b*c))"
print(f'Логическое выражение: {logical_expression}')
postfix_expression = infix_to_postfix(logical_expression)
variables, truth_table = generate_truth_table(postfix_expression)
sknf = sknf_from_truth_table(truth_table, variables)
sdnf = sdnf_from_truth_table(truth_table, variables)
index = index_from_truth_table(truth_table)

print(f"Постфиксная версия: {''.join(postfix_expression)}")
print("Таблица истинности:")
for row in truth_table:
    print(row)
print(f"СКНФ: {sknf}")
print(f"СДНФ: {sdnf}")
#print(f"Индекс Де Моргана: {index}")

