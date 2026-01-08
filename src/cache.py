#cache.py
from collections import deque

class CacheLevel:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity  # number of blocks
        self.queue = deque()      # stores addresses in FIFO order
        self.hits = 0
        self.misses = 0

    def access(self, address):
        """Simulate accessing an address in this cache level."""
        if address in self.queue:
            self.hits += 1
            return True  # hit
        else:
            self.misses += 1
            if len(self.queue) >= self.capacity:
                self.queue.popleft()  # FIFO eviction
            self.queue.append(address)
            return False  # miss

class MultiLevelCache:
    def __init__(self, levels_config):
        """
        levels_config: list of tuples [(name, capacity), ...] e.g. [("L1",4), ("L2",8)]
        """
        self.levels = [CacheLevel(name, cap) for name, cap in levels_config]

    def access(self, address):
        """
        Access an address in the cache hierarchy.
        Returns a string indicating where it hit/missed.
        """
        for level in self.levels:
            if level.access(address):
                return f"{level.name} HIT"
        return "MEMORY MISS"

    def stats(self):
        """Return a dict of hits/misses for each level"""
        return {level.name: {"hits": level.hits, "misses": level.misses} for level in self.levels}

    def print_stats(self):
        print("\nCache Stats:")
        for level in self.levels:
            total = level.hits + level.misses
            hit_rate = (level.hits / total * 100) if total > 0 else 0
            print(f"{level.name}: Hits={level.hits}, Misses={level.misses}, Hit Rate={hit_rate:.2f}%")
