#!/usr/bin/python3
"""Create a class MRUCache that inherits from BaseCaching and is a caching system:
You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: 
super().__init__()
def put(self, key, item):
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):

    def __init__(self):

        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
