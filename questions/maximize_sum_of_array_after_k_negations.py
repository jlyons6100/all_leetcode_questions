# Definition for a binary tree node.
from typing import List
import unittest
from bisect import insort

def largestSumAfterKNegations( A: List[int], K: int) -> int:
    """https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
    """
    negs = []
    pos = []
    for num in A:
        if num < 0:
            insort(negs,num)
        else:
            insort(pos, num)
    while len(negs) != 0:
        if K == 0:
            break
        insort(pos,-negs[0])
        del negs[0]
        K -= 1
    if K % 2 != 0:
        pos[0] = -pos[0]
    return sum(pos) + sum(negs)

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        A = [4,2,3]
        K = 1
        result = largestSumAfterKNegations(A, K)
        self.assertEqual(result, 5)
    def test_2(self):
        A = [2,-3,-1,5,-4]
        K = 2
        result = largestSumAfterKNegations(A, K)
        self.assertEqual(result, 13)
    def test_3(self):
        A = [3, -1, 0, 2]
        K = 3
        result = largestSumAfterKNegations(A, K)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
