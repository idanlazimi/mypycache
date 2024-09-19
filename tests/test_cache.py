import unittest
from mypycache.cache import Cache
from backends.in_memory import InMemoryBackend

class TestCache(unittest.TestCase):
	def setUp(self) -> None:
		self.cache = Cache(InMemoryBackend())

	def test_get_set(self):
		self.cache.set('key', 'value')
		self.assertEqual(self.cache.get('key'), 'value')
	
if __name__ == "__main__":
	unittest.main()