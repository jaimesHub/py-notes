"""Testing something basic"""
import unittest
import pilot


class TestIncrementDecrement(unittest.TestCase):
    """Testing something basic of operators"""

    def test_increment(self):
        """Test increment"""
        self.assertEqual(pilot.increment(3), 4)

    def test_decrement(self):
        """Test decrement"""
        self.assertEqual(pilot.decremnt(3), 4)


if __name__ == "__main__":
    unittest.main()
