import unittest
import config
from algorithms import KthLargest

class TestKthLargest(unittest.TestCase):

    def test_class_instance(self):
        obj = KthLargest([1], 0)
        self.assertIsInstance(obj, KthLargest)

    # Both assertion fails might be unnecessary but I'll leave them because the logic might be useful. :)
    def test_class_instance_fail_by_empty_array(self):
        #obj = KthLargest([], 0)
        with self.assertRaises(AssertionError) as context:
            obj = KthLargest([], 0)
        self.assertTrue('Your array must contain at least 1 number' in str(context.exception))
        
    def test_class_instance_fail_by_k(self):
        #obj = KthLargest([], 0)
        with self.assertRaises(AssertionError) as context:
            obj = KthLargest([1], -1)
        self.assertTrue('Your k value must be a positive integer' in str(context.exception))

    def test_base_case(self):
        obj1 = KthLargest([1], 0)
        obj2 = KthLargest([5], 6)
        self.assertEqual(obj1.base_case(), obj1.arr[0]) 
        self.assertEqual(obj2.base_case(), obj2.arr[0])

    def test_compute_kth(self):
        obj = KthLargest([0,2,3,7,5,6,7], 4)
        self.assertEqual(obj.compute_kth(), 5)

    def test_compute_kth_with_heap(self):
        obj = KthLargest([0,2,3,7,5,6,7], 4)
        self.assertEqual(obj.compute_kth_with_heap(), 5)


if __name__ == '__main__':
    unittest.main()