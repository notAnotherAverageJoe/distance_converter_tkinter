import unittest

def miles_to_km(miles):
    return round(miles * 1.609, 2)

def km_to_miles(km):
    return round(km / 1.609, 2)

class TestDistanceConverter(unittest.TestCase):
    
    def test_miles_to_km(self):
        self.assertEqual(miles_to_km(1), 1.61)
        self.assertEqual(miles_to_km(0), 0)
        self.assertEqual(miles_to_km(5.5), 8.85)
        
    def test_km_to_miles(self):
        self.assertEqual(km_to_miles(1), 0.62)
        self.assertEqual(km_to_miles(0), 0)
        self.assertEqual(km_to_miles(8.85), 5.5)

if __name__ == "__main__":
    unittest.main()
