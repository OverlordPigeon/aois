import pytest
from main import ConstMatrix

@pytest.fixture
def const_matrix():
    return ConstMatrix()

def test_get_value(const_matrix):
    assert const_matrix.get_value(0, 0) == 1
    assert const_matrix.get_value(15, 15) == 0

def test_set_value(const_matrix):
    const_matrix.set_value(0, 0, 0)
    assert const_matrix.get_value(0, 0) == 0
    const_matrix.set_value(15, 15, 1)
    assert const_matrix.get_value(15, 15) == 1

def test_get_word_from_matrix(const_matrix):
    word = const_matrix.get_word_from_matrix(0)
    assert len(word) == 16
    assert word == "1011010000010110"

def test_get_address_row_word(const_matrix):
    row_word = const_matrix.get_address_row_word(0)
    assert len(row_word) == 16
    assert row_word == "1001111000001000"

def test_set_word(const_matrix):
    new_word = "1010101010101010"
    const_matrix.set_word(0, new_word)
    for i in range(16):
        assert const_matrix.get_value(i, 0) == int(new_word[i])

def test_find_word_position(const_matrix):
    assert const_matrix.find_word_position("0000000000000001", True) == 14
    assert const_matrix.find_word_position("1111111111111111", False) == 5

def test_f1_function(const_matrix):
    result = const_matrix.f1_function("1100", "1010")
    assert result == "1000"

def test_f14_function(const_matrix):
    result = const_matrix.f14_function("1100", "1010")
    assert result == "0111"

def test_f3_function(const_matrix):
    result = const_matrix.f3_function("1100", "1010")
    assert result == "1100"

def test_f12_function(const_matrix):
    result = const_matrix.f12_function("1100", "1010")
    assert result == "0011"

def test_summ_ab(const_matrix):
    result = const_matrix.summ_ab("111")
    assert len(result) == 16
    assert result.startswith("111")

if __name__ == "__main__":
    pytest.main()
