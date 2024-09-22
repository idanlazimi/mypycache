import pickle
from backends.base import CacheBackend
import os
import time

class FileBackend(CacheBackend):
	def __init__(self, cachedir: str = 'filecache') -> None:
		self.cache_dir = cachedir
		if not os.path.exists(self.cache_dir):
			os.makedirs(self.cache_dir)
	
	def _get_file_path(self, key: str) -> str:
		return os.path.join(self.cache_dir, f"{key}.cache")
	
	def set(self, key, value, ttl=None):
		file_path = self._get_file_path(key)
		with open(file_path, 'wb') as f:
			pickle.dump((value, ttl, time.time()), f)

	def get(self, key):
		file_path = self._get_file_path(key)
		if not os.path.exists(file_path):
			return None
		with open(file_path, 'rb') as f:
			value, ttl, timestamp = pickle.load(f)
			if ttl and time.time() > timestamp + ttl:
				self.invalidate(key)
				return None
			return value

	def invalidate(self, key):
		file_path = self._get_file_path(key)
		if os.path.exists(file_path):
			os.remove(file_path)

	def clear(self):
		for filename in os.listdir(self.cache_dir):
			file_path = os.path.join(self.cache_dir, filename)
			os.remove(file_path)	
	
	def __len__(self):
		return len(os.listdir(self.cache_dir))