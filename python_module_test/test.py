import unittest
import main

class TestMain(unittest.TestCase):
	def test_do_stuff(self):
		test_param = 10
		result = main.do_stuff(test_param)
		self.assertEqual(result, 15) ##output: ok
		# self.assertEqual(result, 10) ##output: fail

	def test_do_stuff2(self):
		test_param = 'shikjioj'
		result = main.do_stuff(test_param)
		self.assertTrue(isinstance(result, ValueError))  ##output: ok

unittest.main()

#python3 test.py