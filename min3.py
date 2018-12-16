import json, sys

def find_smallest_product( numbers ):
	if len( numbers ) < 3:
		raise ValueError("The input list is short")

	return _find_smallest_product( numbers )

def _find_smallest_product( numbers ):

	smallest_product = [numbers[0], numbers[1], numbers[2], _calc_product(numbers, 0, 1, 2)]

	for i in range( 0, len(numbers) - 2 ):
		for j in range( i+1, len(numbers) - 1 ):
			for k in range( j+1, len(numbers) ):
				actual = _calc_product(numbers, i, j, k)
				if actual < smallest_product[3]:
					smallest_product = [numbers[i], numbers[j], numbers[k], actual]

	return smallest_product

def _calc_product(numbers, i, j, k):
	return numbers[i] * numbers[j] * numbers[k]


def load_numbers( input_file ):
	with open( input_file, "r" ) as input_file_content:
		numbers = json.load(input_file_content)

	return numbers

if __name__ == "__main__":
	numbers = load_numbers( sys.argv[1] )
	smallest_product = find_smallest_product(numbers)
	print(smallest_product)