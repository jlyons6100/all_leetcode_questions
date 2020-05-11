import unittest
from typing import List

def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
	"""implements kids_with_candies
	
	https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

	Find max candies, check if each kid can get at least max candies wit
	extra_candies.
	"""
	max_candies = max(candies)
	result = []
	for n_candies in candies:
		can_have_greatest = n_candies + extra_candies >= max_candies
		result.append(can_have_greatest)
	return result

class TestStringMethods(unittest.TestCase):
	def test_1(self):
		nums = [2, 3, 5, 1, 3]
		extra_candies = 3
		result = kids_with_candies(nums, extra_candies)
		self.assertEqual(result, [True, True, True, False, True])
	def test_2(self):
		nums = [4, 2, 1, 1, 2]
		extra_candies = 1
		result = kids_with_candies(nums, extra_candies)
		self.assertEqual(result, [True, False, False, False, False])
	def test_3(self):
		nums = [12, 1, 12]
		extra_candies = 10
		result = kids_with_candies(nums, extra_candies)
		self.assertEqual(result, [True, False, True])

if __name__ == "__main__":
	unittest.main()
