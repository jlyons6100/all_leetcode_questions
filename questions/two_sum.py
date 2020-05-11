import unittest
from typing import List

def two_sum(nums: List[int], target: List[int]) -> List[int]:
	"""implements two_sum
	
	Definition: Given an numsay of integers, return indices of
	the two numbers such that they add up to a specific target.

	Assumptions: Each input has one solution, you may not use 
	the same element twice

	Intuition: If we store values we've seen, when we come across
	a new value for which target minus new value equals an old value,
	we should have our answer. There are also other ways to solve this.
	Brute force search, sorted + binary search, etc.
	"""
	memo = {}
	for i in range(len(nums)):
		val = target - nums[i]
		if val in memo:
			return [memo[val], i]
		memo[nums[i]] = i

class TestStringMethods(unittest.TestCase):
	def test_1(self):
		nums = [2,7,11,15]
		target = 9
		self.assertEqual(two_sum(nums, target), [0,1])
	def test_2(self):
		nums = [2,7,11,15]
		target = 17
		self.assertEqual(two_sum(nums, target), [0,3])

if __name__ == "__main__":
	unittest.main()
