#!/usr/bin/env python3
""" Class representation of BasicCache.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache that inherits from BaseCaching.
    """

    def __init__(self) -> None:
        """ Initialize basic cache.
        """
        super().__init__()

    def put(self, key, item):
        """ Assign key and item to the cache system.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Fetch data from the cache with key.
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
