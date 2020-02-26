import unittest
import mastercard_code_challenge as mcc


class TestConnection(unittest.TestCase):

    def test_intCheck(self):
        self.assertRaises(ValueError, mcc.code_challenge(1, 'not_integer'))


if __name__ == '__main__':
    unittest.main()
