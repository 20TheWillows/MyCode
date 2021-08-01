import General_Functions
import unittest

class Test_General_Functions(unittest.TestCase):  
    def test_anomalies_overlap_axially_case1(self):
        self.assertEqual(General_Functions.anomalies_overlap_axially(None, 10.1, 2.3, 3.3),None)

    def test_anomalies_overlap_axially_case2(self):
        self.assertEqual(General_Functions.anomalies_overlap_axially(100.5, 1.5,101.99,3.0),True)

    def test_anomalies_overlap_circumferentially_case1(self):
        self.assertEqual(General_Functions.anomalies_overlap_circumferentially(100, 140, 150, 200),False)

    def test_anomalies_overlap_circumferentially_case2(self):
        self.assertEqual(General_Functions.anomalies_overlap_circumferentially(100, 140, 135, 200),True)

    def test_anomalies_overlap_circumferentially_case3(self):
        self.assertEqual(General_Functions.anomalies_overlap_circumferentially(30, 330, 5, 25),False)

    def test_anomalies_overlap_circumferentially_case4(self):
        self.assertEqual(General_Functions.anomalies_overlap_circumferentially(350, 20, 19, 40),True)

    def test_anomalies_overlap_circumferentially_case5(self):
        self.assertEqual(General_Functions.anomalies_overlap_circumferentially(355, 15, 15, 40),True)        

    def test_anomalies_overlap_circumferentially_case6(self):
        self.assertEqual(General_Functions.anomalies_overlap_circumferentially(350, 20, 355, 25),True)

    def test_anomalies_overlap_circumferentially_case7(self):
        self.assertEqual(General_Functions.anomalies_overlap_circumferentially(350, 20, 100, 120),False) 

    def test_anomalies_overlap_circumferentially_case8(self):
        self.assertEqual(General_Functions.anomalies_overlap_circumferentially(350, 20, 350, 20),True) 

class Test_Roman(unittest.TestCase):
    def test_roman_case1(self):
        self.assertEqual(General_Functions.get_roman_year(2000),"MM")
    def test_roman_case2(self):
        self.assertEqual(General_Functions.get_roman_year(1987),"MCMLXXXVII")
    def test_roman_case3(self):
        self.assertEqual(General_Functions.get_roman_year(1650),"MDCL")
    def test_roman_case4(self):
        self.assertEqual(General_Functions.get_roman_year(1999),"MCMXCIX")
if __name__ == '__main__':
    unittest.main()