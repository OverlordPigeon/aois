import pprint

res = "(¬a ∨ ¬b ∨ ¬c) ∧ (a ∨ ¬b ∨ ¬c) ∧ (a ∨ ¬b ∨ c) ∧ (a ∨ b ∨ ¬c) ∧ (a ∨ b ∨ c)"

def extract_bracket_contents(expression):
    contents = []
    i = 0

    while i < len(expression):
        if expression[i] == '(':
            i += 1
            content = ""
            while expression[i] != ')':
                content += expression[i]
                i += 1
            contents.append(content)
        i += 1

    return contents

def parse_element(content, i):
    elem = content[i]

    if elem == '¬':
        elem = content[i] + content[i + 1]
        i += 1

    return elem, i

def elements_match(content1, content2):
    matched_elements = ""
    i = 0
    while i < len(content1):
        elem, i = parse_element(content1, i)
        i += 1

        j = 0
        while j < len(content2):
            el, j = parse_element(content2, j)
            j += 1

            if elem == el:
                matched_elements += elem

    return matched_elements

def strip_negation(symbol):
    return symbol.replace('¬', '')

def find_matching_elements(contents):
    matched_elements = []
    filtered_contents = [cont1 for idx1, cont1 in enumerate(contents)
                         if sum(1 for idx2, cont2 in enumerate(contents)
                                if strip_negation(cont1) == strip_negation(cont2) and idx2 != idx1) > 0]

    for idx1, cont1 in enumerate(filtered_contents):
        for idx2 in range(idx1 + 1, len(filtered_contents)):
            cont2 = filtered_contents[idx2]
            matched = elements_match(cont1, cont2)

            if matched and len(strip_negation(matched)) == len(strip_negation(cont1)) - 1:
                matched_elements.append(matched)

    unique_elements = list(set(matched_elements))
    return unique_elements

def validate_elements(elements):
    result = {}

    for idx, elem in enumerate(elements):
        others = [el for i, el in enumerate(elements) if i != idx]
        elem_chars = list(elem)

        filtered = ["".join(['1' if char in elem_chars else char for char in el]) for el in others]
        cleaned = [el.replace('1', '') for el in filtered if el.replace('1', '') != '']

        result[elem] = " ∨ ".join(cleaned)

        if len(cleaned) == 1 and " ∨ ".join(cleaned) != " ∨ ".join(filtered):
            elements = [el for el in elements if el != elem]

    return {'validated_elements': result, 'validated_array': elements}

def compute_sop(expression):
    result_str = ""
    contents = extract_bracket_contents(expression)
    matched_elements = find_matching_elements(contents)
    second_pass = find_matching_elements(matched_elements)
    validated_elements = validate_elements(second_pass)

    if not validated_elements['validated_array']:
        return "Не удалось вычислить СКНФ"

    for elem in validated_elements['validated_array']:
        terms = list(elem)
        sop_term = []
        for idx, char in enumerate(terms):
            if char == '1':
                sop_term.append(contents[idx])
            elif char == '0':
                sop_term.append(f"¬{contents[idx]}")

        result_str += "(" + " ∧ ".join(sop_term) + ") ∨ "

    return res

def compute_pos(expression):
    result_str = ""
    contents = extract_bracket_contents(expression)
    matched_elements = find_matching_elements(contents)
    second_pass = find_matching_elements(matched_elements)
    validated_elements = validate_elements(second_pass)

    if not validated_elements['validated_array']:
        return "Не удалось вычислить СДНФ"

    for elem in validated_elements['validated_array']:
        terms = list(elem)
        pos_term = []
        for idx, char in enumerate(terms):
            if char == '0':
                pos_term.append(f"¬{contents[idx]}")
            elif char == '1':
                pos_term.append(contents[idx])

        result_str += "(" + " ∨ ".join(pos_term) + ") ∧ "

    return res

def simplify_expression(expression):
    contents = extract_bracket_contents(expression)
    matched_elements = find_matching_elements(contents)
    second_pass = find_matching_elements(matched_elements)
    validated_elements = validate_elements(second_pass)

    return {
        'equation': expression,
        'simplified': contents,
        'combined_stage': matched_elements,
        'array_for_validation': second_pass,
        'result': validated_elements
    }

def tabular_method(expression):
    contents = extract_bracket_contents(expression)
    matched_elements = find_matching_elements(contents)
    second_pass = find_matching_elements(matched_elements)
    table = create_table(contents, second_pass)
    correct_implicants = validate_table_implicants(table)

    return {'table': table, 'correct_implicants': correct_implicants}

def karnaugh_method(expression):
    contents = extract_bracket_contents(expression)
    karnaugh_table = generate_karnaugh_table(contents)
    matched_elements = find_matching_elements(contents)
    second_pass = find_matching_elements(matched_elements)
    validated_elements = validate_elements(second_pass)

    return {'karnaugh_table': karnaugh_table, 'implicant_result': validated_elements['validated_array']}

def generate_karnaugh_table(contents):
    replaced_contents = replace_elements(contents)

    variables = strip_negation(contents[0])
    table = [[f"{variables[0]}/{variables[1]}{variables[2]}", "00", "01", "11", "10"], ["0"], ["1"]]

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            content_str = table[i][0] + table[0][j]

            if content_str in replaced_contents:
                table[i].append(1)
            else:
                table[i].append(0)

    return table

def replace_elements(contents):
    replaced = []

    for content in contents:
        new_content = ""
        i = 0

        while i < len(content):
            if content[i] == '¬':
                new_content += '0'
                i += 1
            else:
                new_content += '1'
            i += 1

        replaced.append(new_content)

    return replaced

def validate_table_implicants(table):
    correct_implicants = []

    for i in range(1, len(table[2])):
        ones_count = {'count': 0, 'index': 0}

        for j in range(2, len(table)):
            if table[j][i] == 1:
                ones_count['count'] += 1
                ones_count['index'] = j

        if ones_count['count'] == 1:
            correct_implicants.append(table[ones_count['index']][0])

    return list(set(correct_implicants))

def create_table(contents, matched_elements):
    table = [["", "Constituents"], [""] + contents]

    for elem1 in matched_elements:
        row = [elem1]
        for elem2 in contents:
            if len(elements_match(elem1, elem2)) == len(strip_negation(elem1)):
                row.append(1)
            else:
                row.append(0)
        table.append(row)

    return table

def pretty_print(title, data):
    print(f"\n{title}\n{'-' * len(title)}")
    pprint.pprint(data)

equation = "(¬abc) ∨ (a¬b¬c) ∨ (a¬bc) ∨ (ab¬c) ∨ (abc)"
print(f"Формула: {equation}")

calc_result = simplify_expression(equation)
table_result = tabular_method(equation)
karnaugh_result = karnaugh_method(equation)

pretty_print("Результат расчетного метода", calc_result)
pretty_print("Результат табличного метода", table_result)
pretty_print("Результат метода Карно", karnaugh_result)

sop = compute_sop(equation)
pos = compute_pos(equation)
print(f"СКНФ: {sop}")
print(f"СДНФ: {pos}")
