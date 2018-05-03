import unittest 
#from src.calcul_v1 import Calcul
from src.calcul_v2 import Calcul

class TestCases(unittest.TestCase): 

    def test(self): 
        calcul = Calcul() 

        self.assertEqual(calcul.traduitSecondes(90000000), "2 ans 311 jours 16 heures 0 minutes 0 secondes")
        
        self.assertEqual(calcul.traduitSecondes(63508215), "2 ans 5 jours 1 heures 10 minutes 15 secondes")

if __name__ == '__main__': 
    unittest.main() 