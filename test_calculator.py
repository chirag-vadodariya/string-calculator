import unittest;
from calculator import Calculator;

class TestCalculator(unittest.TestCase):
    def test_empty_string(self):
        calc = Calculator();
        self.assertEqual(calc.add(""), 0);
        
    def test_single_number(self):
        calc = Calculator();
        self.assertEqual(calc.add("1"), 1);
        
    def testmultiple_numbers(self):
        calc = Calculator();
        self.assertEqual(calc.add("1,2,3"), 6);
        
    def test_newline_between_numbers(self):
        calc = Calculator();
        self.assertEqual(calc.add("1\n2,3"), 6);
        
    def testCustomDelimiter(self):
        calc = Calculator();
        self.assertEqual(calc.add("//;\n1;2"), 3);
        
    def testNegativeNumbers(self):
        calc = Calculator();
        with self.assertRaises(ValueError) as exc_info:
            calc.add("-1,2,-3");
        self.assertEqual(str(exc_info.exception), "Negatives not allowed: -1, -3");
        
if __name__ == '__main__':
    unittest.main();