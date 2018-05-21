import unittest

class TestYT(unittest.TestCase):
	def setUp(self):
		print('some text')

	def test_API_Youtube(self):
		print('some vidio')

	def tearDown(self):
		print('some text1')

if __name__ == "__main__":
	unittest.main()
	
