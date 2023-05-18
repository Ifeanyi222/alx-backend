#!/usr/bin/python3
"""Create a class BasicCache that inherits from BaseCaching 
and is a caching system:
You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def __init__(self):
    
        super().__init__()

    def put(self, key, item):
    
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
    
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
