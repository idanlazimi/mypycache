from abc import ABC, abstractmethod

class CacheBackend(ABC):
    @abstractmethod
    def set(self, key, value, ttl=None):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def invalidate(self, key):
        pass

    @abstractmethod
    def clear(self):
        pass
    
    @abstractmethod
    def __len__(self):
        pass