import unittest
import config
from algorithms import Anagram

class TestAnagram(unittest.TestCase):

    def test_class_instance(self):
        obj = Anagram('hello','friend')
        self.assertIsInstance(obj, Anagram)

    def test_base_case(self):
        obj = Anagram('my','bad')
        self.assertFalse(obj.base_case()) 

    # def test_compute_kth(self):
    #     obj = TestAnagram([0,2,3,7,5,6,7], 4)
    #     self.assertEqual(obj.compute_kth(), 5)

    # def test_compute_kth_with_heap(self):
    #     obj = TestAnagram([0,2,3,7,5,6,7], 4)
    #     self.assertEqual(obj.compute_kth_with_heap(), 5)

if __name__ == '__main__':
    unittest.main()