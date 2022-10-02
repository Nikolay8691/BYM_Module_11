print('hello! this is a test program')

import unittest

import merge_sort

class Tests(unittest.TestCase):
	"""testing 'merge' sorting function"""

	def test_1(self):
		"""testing 'merge' sorting function compare to standart function 'sorted'"""
		a = merge_sort.a
		b = merge_sort.b
		self.assertEqual(b, sorted(a))

	def test_2(self):
		"""testing 'merge' sorting function whether it raises number with every step"""
		n = len(merge_sort.a)
		b = merge_sort.b
		j = 1
		for i in range(n - 1):
			if b[i] <= b[i+1]:
				j += 1
			else:
				break
		self.assertEqual(j, n)


	def test_3(self):
		"""testing 'merge' sorting function whether [0] element is min"""
		a = merge_sort.a
		b = merge_sort.b
		amin = a[0]
		bmin = b[0]
		self.assertTrue(amin >= bmin)		

	def test_4(self):
		"""testing 'merge' sorting function whether [-1] element is max"""
		a = merge_sort.a
		b = merge_sort.b
		amax = a[-1]
		bmax = b[-1]
		self.assertFalse(amax > bmax)

if __name__ == "__main__":
	unittest.main()
