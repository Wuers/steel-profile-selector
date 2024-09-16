import unittest
from structural_analisis import calculate_moment

class TestAnalysis(unittest.TestCase):
    def test_calculate_moment(self):
        self.assertEqual(calculate_moment(20, 5), 62.5)
        
if __name__ == "__main__":
    unittest.main()
