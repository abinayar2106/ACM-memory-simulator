#allocator.py
from cache import MultiLevelCache
cache_system = MultiLevelCache([("L1", 4),("L2",8)])
current_allocator = "first_fit"
def set_allocator(allocator_type):
    global current_allocator
    if allocator_type in ["first_fit", "best_fit", "worst_fit"]:
        current_allocator = allocator_type
        print(f"Allocator set to {allocator_type}")
    else:
        print("Unknown allocator type.")

class Block:
    def __init__(self, start, size, free=True, id=None):
        self.start = start
        self.size = size
        self.free = free
        self.id = id

memory = []  # Global memory list
next_block_id = 1  # Global counter for assigned IDs

def init_memory(size):
    global memory, next_block_id
    memory = [Block(0, size)]
    next_block_id = 1
    print(f"Initialized memory of size {size}.")

def allocate(request_size):
    global next_block_id

    selected_index = None

    if current_allocator == "first_fit":
        for i, block in enumerate(memory):
            if block.free and block.size >= request_size:
                selected_index = i
                break

    elif current_allocator == "best_fit":
        best_size = float('inf')
        for i, block in enumerate(memory):
            if block.free and block.size >= request_size and block.size < best_size:
                best_size = block.size
                selected_index = i

    elif current_allocator == "worst_fit":
        worst_size = -1
        for i, block in enumerate(memory):
            if block.free and block.size >= request_size and block.size > worst_size:
                worst_size = block.size
                selected_index = i

    if selected_index is None:
        print("Allocation failed: Not enough memory.")
        return None

    # Allocate block (splitting logic same as before)
    block = memory[selected_index]
    block_id = next_block_id
    next_block_id += 1

    if block.size > request_size:
        new_block = Block(
            start=block.start + request_size,
            size=block.size - request_size,
            free=True
        )
        memory.insert(selected_index + 1, new_block)
        block.size = request_size
    

    block.free = False
    block.id = block_id
    cache_system.access(block.start)
    print(f"Allocated block id={block_id} at address={block.start}")
    return block_id


def dump_memory():
    print("\nCurrent Memory Layout:")
    used = 0
    free = 0
    largest_free = 0

    for block in memory:
        status = "FREE" if block.free else f"USED (id={block.id})"
        print(f"[{block.start} - {block.start + block.size - 1}] {status}")

        if block.free:
            free += block.size
            if block.size > largest_free:
                largest_free = block.size
        else:
            used += block.size

    external_frag = 0
    if free > 0:
        external_frag = 1 - (largest_free / free)

    print("\nMemory Stats:")
    print(f"Total memory: {used + free}")
    print(f"Used memory: {used}")
    print(f"Free memory: {free}")
    print(f"Largest free block: {largest_free}")
    print(f"External fragmentation: {external_frag:.2%}\n")


def free_block(block_id):
    found = False
    for i, block in enumerate(memory):
        if not block.free and block.id == block_id:
            block.free = True
            block.id = None
            cache_system.access(block.start) #simulate cache access for deallocation
            found = True
            print(f"Block {block_id} freed.")
            
            # Coalesce with next block
            if i + 1 < len(memory):
                next_block = memory[i + 1]
                if next_block.free:
                    block.size += next_block.size
                    memory.pop(i + 1)

            # Coalesce with previous block
            if i - 1 >= 0:
                prev_block = memory[i - 1]
                if prev_block.free:
                    prev_block.size += block.size
                    memory.pop(i)
            break
    if not found:
        print(f"Block {block_id} not found.")
