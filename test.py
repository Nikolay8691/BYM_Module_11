print('hello! this is a test program')

import unittest

import merge_sort

class Tests(unittest.TestCase):
	"""testing 'merge' sorting function"""

	def test_1(self):
		a = merge_sort.a
		b = merge_sort.b
		self.assertEqual(b, sorted(a))

	def test_2(self):
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
		a = merge_sort.a
		b = merge_sort.b
		amin = a[0]
		bmin = b[0]
		self.assertTrue(amin >= bmin)		

	def test_4(self):
		a = merge_sort.a
		b = merge_sort.b
		amax = a[len(a)-1]
		bmax = b[len(b)-1]
		self.assertFalse(amax > bmax)

if __name__ == "__main__":
	unittest.main()
