import unittest

import lib_calc


class TddTest(unittest.TestCase):

    def testAdd(self):
        result = lib_calc.add(10, 20)

        # 결과 값이 일치 여부 확인
        self.assertEqual(result, 31)

    def testSubstract(self):
        result = lib_calc.substract(20, 10)

        if result > 10:
            boolval = True
        else:
            boolval = False

        # 결과 값이 True 여부 확인
        self.assertTrue(boolval)

    def testDivision(self):
        # 결과 값이 ZeroDivisionError 예외 발생 여부 확인
        self.assertRaises(ZeroDivisionError, lib_calc.division, 4, 1)

    def testMultiply(self):
        nonechk = True

        result = lib_calc.multiply(10, 9)

        if result > 100:
            nonechk = None

        # 결과 값이 None 여부 확인
        self.assertIsNone(nonechk)

if __name__ == '__main__':
    unittest.main()