import unittest;
from calculator import Calculator;

class TestCalculator(unittest.TestCase):
    def test_empty_string(self):
        calc = Calculator();
        self.assertEqual(calc.add(""), 0);
        
    def test_newline_between_numbers(self):
        calc = Calculator();
        self.assertEqual(calc.add("1\n2,3"), 6);
        
if __name__ == '__main__':
    unittest.main();