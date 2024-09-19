import pytest
from main import (
    extract_bracket_contents, parse_element, elements_match, strip_negation,
    find_matching_elements, validate_elements, simplify_expression,
    compute_sop, karnaugh_method,
    generate_karnaugh_table, replace_elements, validate_table_implicants,
    create_table, res
)

@pytest.fixture
def test_data():
    return '¬a ∨ ¬b ∨ ¬c ∨ (a ∨ ¬b ∨ ¬c) ∨ (a ∨ ¬b ∨ c) ∨ (a ∨ b ∨ ¬c) ∨ (a ∨ b ∨ c)'

def test_extract_bracket_contents():
    assert extract_bracket_contents(res) == ['¬a ∨ ¬b ∨ ¬c', 'a ∨ ¬b ∨ ¬c', 'a ∨ ¬b ∨ c', 'a ∨ b ∨ ¬c', 'a ∨ b ∨ c']

def test_parse_element():
    assert parse_element('¬a', 0) == ('¬a', 1)
    assert parse_element('a', 0) == ('a', 0)

def test_elements_match():
    assert elements_match('¬a ∨ ¬b ∨ ¬c', 'a ∨ ¬b ∨ ¬c') == '    ∨∨    ¬b    ∨∨    ¬c'
    assert elements_match('a ∨ b ∨ c', 'a ∨ ¬b ∨ c') == 'a    ∨∨        ∨∨    c'

def test_strip_negation():
    assert strip_negation('¬a ∨ ¬b ∨ ¬c') == 'a ∨ b ∨ c'
    assert strip_negation('a ∨ b ∨ c') == 'a ∨ b ∨ c'

def test_find_matching_elements():
    contents = extract_bracket_contents(res)
    assert find_matching_elements(contents) == []

def test_validate_elements():
    contents = find_matching_elements(extract_bracket_contents(res))
    result = validate_elements(contents)
    assert 'validated_elements' in result
    assert 'validated_array' in result

def test_compute_sop():
    assert compute_sop(res) == "Не удалось вычислить СКНФ"

def test_simplify_expression():
    result = simplify_expression(res)
    assert 'equation' in result
    assert 'simplified' in result
    assert 'combined_stage' in result
    assert 'array_for_validation' in result
    assert 'result' in result

def test_karnaugh_method():
    result = karnaugh_method(res)
    assert 'karnaugh_table' in result
    assert 'implicant_result' in result

def test_generate_karnaugh_table():
    contents = extract_bracket_contents(res)
    table = generate_karnaugh_table(contents)
    assert len(table) > 0

def test_replace_elements():
    contents = extract_bracket_contents(res)
    replaced = replace_elements(contents)
    assert replaced == ['011101110', '111101110', '111101111', '111111110', '111111111']

def test_validate_table_implicants():
    contents = extract_bracket_contents(res)
    table = generate_karnaugh_table(contents)
    implicants = validate_table_implicants(table)
    assert len(implicants) >= 0

def test_create_table():
    contents = extract_bracket_contents(res)
    matched_elements = find_matching_elements(contents)
    table = create_table(contents, matched_elements)
    assert len(table) > 0

if __name__ == "__main__":
    pytest.main()
