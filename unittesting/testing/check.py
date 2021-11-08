import unittest
from testrun import check
class Test(unittest.TestCase):
    def testone(self):
        self.assertEqual(check(-2,-1,0),0)
    def testtwo(self):
        self.assertEqual(check('a',9,0),"error")
    def testhree(self):
        self.assertEqual(check(1, 1, 1), 1)
    def testfour(self):
        self.assertEqual(check(0,0,4), 4)
    def testfive(self):
        self.assertEqual(check(-2,-5,0.8), 0.8)
    def testsix(self):
        self.assertEqual(check(1, -1.7, 1), 1)
    def testseven(self):
        self.assertEqual(check(1.2, 1.7, 0.1), 1.7)
    def testeight(self):
        self.assertEqual(check(9.3,"hello",0),"error")
    def testnine(self):
        self.assertEqual(check("test","hello",10),"error")
    def testten(self):
        self.assertEqual(check(9.3,2,-1.7),9.3)
    def test11(self):
        self.assertEqual(check(0,0,-10), 0)
    def test12(self):
        self.assertEqual(check(0,-0.2,-1000000), 0)
    def test13(self):
        self.assertEqual(check(10000000000,0,-200),10000000000)
    def test14(self):
        self.assertEqual(check(-10000000000,0,-0.021588515151),0)
    def test15(self):
        self.assertEqual(check(-1,0.0000001,-2),0.0000001)
    def test16(self):
        self.assertEqual(check(0.1,0.1,0.1),0.1)
    def test17(self):
        self.assertEqual(check(-10000000000,-100000000000,-1000000000000000),-10000000000)
    def test18(self):
        self.assertEqual(check(0.1111111111,0.2222222222222222222,0.0000111111222222),0.2222222222222222222)
    def test19(self):
        self.assertEqual(check(1000,1000,1000),1000)
    def test20(self):
        self.assertEqual(check(0.01,-10000,-1),0.01)
    def test21(self):
        self.assertEqual(check('@',8,4),"error")
    def test22(self):
        self.assertEqual(check('8','1',4),"error")
    def testlargest1(self):
        self.assertEqual(check(0, 0, 0), 0)
    def testlargest2(self):
        self.assertEqual(check(-1, 1, 2), 2)
    def testlargest3(self):
        self.assertEqual(check(10, 3, 9), 10)
    def testlargest4(self):
        self.assertEqual(check("A", 3, 4), "error")
    def testlargest5(self):
        self.assertEqual(check(-1, -5, -3), -1)
    def testlargest6(self):
        self.assertEqual(check(2.5, 5.6, 7.3), 7.3)
