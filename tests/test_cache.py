import unittest
from mypycache.cache import Cache
from backends.in_memory import InMemoryBackend
from backends.file import FileBackend
import time

class TestCache(unittest.TestCase):
	def setUp(self) -> None:
		self.cache_types = [
			(Cache(InMemoryBackend()), "InMemoryBackend"),
			(Cache(FileBackend()), "FileBackend")
		]

	def test_get_set(self):
		for cache, backend_name in self.cache_types:
			with self.subTest(backend=backend_name):
				cache.set('key', 'value')
				self.assertEqual(cache.get('key'), 'value')

	def test_ttl(self):		
		for cache, backend_name in self.cache_types:
			with self.subTest(backend=backend_name):
				cache.set('key1', 'value', ttl=3)
				time.sleep(4)
				self.assertEqual(cache.get('key1'), None)

	def test_clear(self):
		for cache, backend_name in self.cache_types:
			with self.subTest(backend=backend_name):
				cache.set('key2', 'value', ttl=3)
				cache.clear()
				self.assertEqual(cache.get('key2'), None)

	def test_invalid(self):
		for cache, backend_name in self.cache_types:
			with self.subTest(backend=backend_name):
				cache.set('key3', 'value', ttl=3)
				cache.invalidate('key3')
				self.assertEqual(cache.get('key3'), None)
				
	def test_len(self):
		for cache, backend_name in self.cache_types:
			with self.subTest(backend=backend_name):
				cache.clear()
				cache.set('key3', 'value', ttl=3)
				cache.set('key4', 'value', ttl=3)
				cache.set('key5', 'value', ttl=3)
				self.assertEqual(len(cache), 3)
	
if __name__ == "__main__":
	unittest.main()