import unittest
from main import *


class Tests(unittest.TestCase):

    def test_operator_precedence(self):
        self.assertTrue(operator_precedence('*', '+'))
        self.assertTrue(operator_precedence('!', '('))
        self.assertFalse(operator_precedence('+', '*'))

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix('a+b*c'), ['a', 'b', 'c', '*', '+'])
        self.assertEqual(infix_to_postfix('(a+b)*c'), ['a', 'b', '+', 'c', '*'])

    def test_evaluate_postfix(self):
        var_dict = {'A': True, 'B': False, 'C': True}
        self.assertEqual(evaluate_postfix(['A', 'C', '*'], var_dict), '1')  # False
        self.assertEqual(evaluate_postfix(['A', 'B', '+'], var_dict), '1')  # True
        self.assertEqual(evaluate_postfix(['A', 'B', 'C', '+', '*'], var_dict), '1')  # True

    def test_generate_truth_table(self):
        postfix_expr = ['A', 'B', '*', 'C', '+']
        variables, table = generate_truth_table(postfix_expr)
        self.assertEqual(variables, ['A', 'B', 'C'])
        expected_table = [
            ['0', '0', '0', '0'],
            ['0', '0', '1', '0'],
            ['0', '1', '0', '0'],
            ['0', '1', '1', '0'],
            ['1', '0', '0', '1'],
            ['1', '0', '1', '1'],
            ['1', '1', '0', '1'],
            ['1', '1', '1', '1']
        ]

        self.assertEqual(table, expected_table)

    def test_sknf_from_truth_table(self):
        truth_table = [
            ['0', '0', '0', '0'],
            ['0', '0', '1', '0'],
            ['0', '1', '0', '0'],
            ['0', '1', '1', '1'],
            ['1', '0', '0', '0'],
            ['1', '0', '1', '0'],
            ['1', '1', '0', '0'],
            ['1', '1', '1', '1']
        ]
        variables = ['A', 'B', 'C']
        sknf = sknf_from_truth_table(truth_table, variables)
        expected_sknf = '(ABC) + (AB!C) + (A!BC) + (!ABC) + (!AB!C) + (!A!BC)'
        self.assertEqual(sknf, expected_sknf)

    def test_sdnf_from_truth_table(self):
        truth_table = [
            ['0', '0', '0', '0'],
            ['0', '0', '1', '0'],
            ['0', '1', '0', '0'],
            ['0', '1', '1', '1'],
            ['1', '0', '0', '0'],
            ['1', '0', '1', '0'],
            ['1', '1', '0', '0'],
            ['1', '1', '1', '1']
        ]
        variables = ['A', 'B', 'C']
        sdnf = sdnf_from_truth_table(truth_table, variables)
        expected_sdnf = '(!ABC) * (ABC)'
        self.assertEqual(sdnf, expected_sdnf)

    def test_index_from_truth_table(self):
        truth_table = [
            ['0', '0', '0', '0'],
            ['0', '0', '1', '0'],
            ['0', '1', '0', '0'],
            ['0', '1', '1', '1'],
            ['1', '0', '0', '0'],
            ['1', '0', '1', '0'],
            ['1', '1', '0', '0'],
            ['1', '1', '1', '1']
        ]
        index = index_from_truth_table(truth_table)
        expected_index = 17
        self.assertEqual(index, expected_index)

if __name__ == '__main__':
    unittest.main()
