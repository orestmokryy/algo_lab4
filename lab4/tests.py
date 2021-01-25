import unittest
from util import algorithm


class AlgorithmTester(unittest.TestCase):

    def test_1(self):
        self.assertEqual(algorithm('first_input.txt'), 3)

    def test_2(self):
        self.assertEqual(algorithm('second_input.txt'), 1)

    def test_3(self):
        self.assertEqual(algorithm('third_input.txt'), 1)



    #
    # def test_4(self):
    #     self.assertEqual(algorithm('fourth_input.txt'), 5)


if __name__ == '__main__':
    unittest.main()
