

from unittest import TestCase
import min3


class min3_Test(TestCase):

	def test_smallest_product(self):
		test_data = [
			{
				"input": [-10, 2, 3, 5],
				"expected": [-10, 3, 5, -150]
			},
			{
				"input": [-10, 2, 3],
				"expected": [-10, 2, 3, -60]
			},
			{
				"input": [1, 1, 1],
				"expected": [1, 1, 1, 1]
			},
			{
				"input": [-1, -1, -1],
				"expected": [-1, -1, -1, -1]
			},
			{
				"input": [0, 1, 1],
				"expected": [0, 1, 1, 0]
			},
			{
				"input": [-1, 1, 1],
				"expected": [-1, 1, 1, -1]
			}
		]

		for item in test_data:
			smallest_product = min3.find_smallest_product(item["input"])
			self.assertEqual(smallest_product, item["expected"])

	def test_smallest_product_with_short_input(self):
		self.assertRaises(ValueError, min3.find_smallest_product, [-10, 2])


