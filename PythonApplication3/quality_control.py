import doctest
import sys

def fib(n):
    '''
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10) 
    55
    >>> fib(15)
    610
    >>> 

    '''
    a, b = 0,1
    for i in range(n):
        a, b = b, a+b
        print(a)
    print('Sum :',a)

if __name__== '__main__':
    doctest.testmod()
   # fib(int(sys.argv[1]))

# what i think is in python 3.7 we don't need this to pass argument from cmd
    

#https://www.python-course.eu/python3_tests.php
#https://docs.python.org/3/tutorial/stdlib.html

import unittest
'''
    class TestStatisticalFunction(unittest.TestCase):

        def test_average(self):
            self.assertEqual(average([20, 30, 70]), 40.0)
            self.assertEqual(round(average([1,5,7 ],1), 4.3)
            with self.assertRaises(ZeroDivisionError):
                average([])
            with self.assertRaise(TypeError):
                average(20, 30 ,70)

    unittest.main()
'''
class FibonacciTest(unittest.TestCase):

    def testCalculation(self):
       # self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)

if __name__ == '__main__':
    unittest.main()