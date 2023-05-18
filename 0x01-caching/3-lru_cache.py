#!/usr/bin/python3
"""Create a class LRUCache that inherits from BaseCaching and is a caching system:
You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: 
super().__init__()
def put(self, key, item):
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):

    def __init__(self):
        
        super().__init__()
        self.queue = []

    def put(self, key, item):
        
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
    
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
