import unittest
import mastercard_code_challenge as mcc


class TestConnection(unittest.TestCase):

    def test_intCheck(self):
        self.assertRaises(ValueError, mcc.information_check(1, 'not_integer'))

    def test_connectionTest(self):
        self.assertFalse(False, mcc.connection_check(500))


if __name__ == '__main__':
    unittest.main()
