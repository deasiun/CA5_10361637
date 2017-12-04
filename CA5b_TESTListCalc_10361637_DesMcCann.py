import unittest
from CA5b_ListCalc_10361637_DesMcCann import cal
# test the calculator functionality

a= [2,4,6,8,10]
b= [1,2,3]
c= [20,10,5]
d= [40,20]

class TestCalculator(unittest.TestCase):
#defining some lists for use.


    def setUp(self):
        self.calc = cal()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add([2,4,6,8,10])
        self.assertEqual(30, result)
        result = self.calc.add([2,4])
        self.assertEqual(6, result)
        result = self.calc.add([1,2,4])
        self.assertEqual(7, result)

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(c)
        self.assertEqual(5, result)
        result = self.calc.subtract(b)
        self.assertEqual(-4, result)
        result = self.calc.subtract(d)
        self.assertEqual(20, result)
        
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply([2,2])
        self.assertEqual(4, result)
        result = self.calc.multiply([2,3,4])
        self.assertEqual(24, result)
        result = self.calc.multiply(c)
        self.assertEqual(1000, result)
        
    def test_calculator_intdivide_method_returns_correct_result(self):
        result = self.calc.intdivide([2,2])
        self.assertEqual(1, result)
        result = self.calc.intdivide([40,4,2])
        self.assertEqual(5, result)
        result = self.calc.intdivide([16,-4,4])
        self.assertEqual(-1, result)
        
    def test_calculator_remainder_method_returns_correct_result(self):
        result = self.calc.remainder([5,2])
        self.assertEqual(1, result)
        result = self.calc.remainder([59,6,5])
        self.assertEqual(0, result)
        result = self.calc.remainder([11,4,2])
        self.assertEqual(1, result)       
        
    def test_calculator_fdivision_method_returns_correct_result(self):
        result = self.calc.fdivision([5.0,2.0])
        self.assertEqual(2.5, result)
        result = self.calc.fdivision([12.0,3.0,2.0])
        self.assertEqual(2.0, result)
        result = self.calc.fdivision([72.0,8.0,4.0])
        self.assertEqual(2.25, result)         
    
    def test_calculator_signchange_method_returns_correct_result(self):
        result = self.calc.signchange([-90,56,-700])
        self.assertEqual([90,-56,700], result)
        result = self.calc.signchange([-1,3,-6])
        self.assertEqual([1,-3,6], result)          
    
    def test_calculator_absolute_method_returns_correct_result(self):
        result = self.calc.absolute([-90,56,-700])
        self.assertEqual([90,56,700], result)
        result = self.calc.absolute([-1,3,-6])
        self.assertEqual([1,3,6], result)        
        
 
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square([2,4,6])
        self.assertEqual([4,16,36], result)
        result = self.calc.square([-2,2])
        self.assertEqual([4,4], result)
        result = self.calc.square([-1.5,3,5])
        self.assertEqual([2.25,9,25], result)          

        
    def test_calculator_squareroot_method_returns_correct_result(self):
        result = self.calc.squareroot([9,4])
        self.assertEqual([3,2], result)
        result = self.calc.squareroot([16,25,36])
        self.assertEqual([4,5,6], result)
     
       
    def test_calculator_factorial_method_returns_correct_result(self):
        result = self.calc.factorial([3,4,5])
        self.assertEqual([6,24,120], result)
        result = self.calc.factorial([5,2,1])
        self.assertEqual([120,2,1], result)
    
if __name__ == '__main__':
    unittest.main()


