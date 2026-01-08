#cache.py
from collections import deque

class CacheLevel:
    def __init__(self, name, capacity, block_size, associativity):
        self.name = name
        self.capacity = capacity
        self.block_size = block_size
        self.associativity = associativity
        self.queue = deque()
        self.hits = 0
        self.misses = 0

    def access(self, address):
        if address in self.queue:
            self.hits += 1
            return True
        else:
            self.misses += 1
            return False

    def insert(self, address):
        if len(self.queue) >= self.capacity:
            evicted = self.queue.popleft()
            print(f"{self.name} Cache evicting address {evicted}")
        self.queue.append(address)

class MultiLevelCache:
    def __init__(self, levels_config, block_size, associativity):
        self.levels = [
            CacheLevel(name, cap, block_size, associativity)
            for name, cap in levels_config
        ]

    def access(self, address):
        for level in self.levels:
            if level.access(address):
                print(f"Cache HIT at {level.name} for address {address}")
                return level.name

        print(f"Cache MISS at all levels -> Accessing Main Memory for address {address}")

        for level in self.levels:
            level.insert(address)

        return "MEMORY"
    def dump(self):
        print("\nCache Contents:")
        for level in self.levels:
            print(f"{level.name}: {list(level.queue)}")


    def stats(self):
        """Return a dict of hits/misses for each level"""
        return {level.name: {"hits": level.hits, "misses": level.misses} for level in self.levels}

    def print_stats(self):
        print("\nCache Stats:")
        for level in self.levels:
            total = level.hits + level.misses
            hit_rate = (level.hits / total * 100) if total > 0 else 0
            print(f"{level.name}: Hits={level.hits}, Misses={level.misses}, Hit Rate={hit_rate:.2f}%")
