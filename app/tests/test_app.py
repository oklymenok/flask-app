import unittest

class TestApp(unittest.TestCase):
    """Unit tests placeholder to test AWS CI/CD"""

    def test_placeholder(self):
        """Test return backwards simple string"""
        string_a = "hello world"
        string_b = "hello world"
        self.assertEqual(string_a, string_b)

if __name__ == "__main__":
    unittest.main()