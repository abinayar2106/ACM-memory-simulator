### MEMORY MANAGEMENT SIMULATOR - DESIGN DOC.

1. Overview
This project implements a user-space memory management simulator that models how an OS allocates and deallocates memory at runtime.The simulator supports multiple dynamic memory allocation strategies and includes a multilevel CPU cache simulation to track memory access behavior.

The goal of the project to simulate core OS memory-management concepts using well-defined data structures and algorithms(even if a real OS kernel is not the main focus)

2. Memory Model and Assumptions
Physical memory is simulated as a single continuous block of configurable size.(1024, in this case)
Memory is represented as a list of blocks, where each block has a:
 -Starting address
 -Size
 -Allocation status (free / allocated)
 -Block ID (for allocated blocks)
Memory addresses are simulated as integer offsets from a base address (0).

This abstraction allows the simulator to model allocation, deallocation, and fragmentation without relying on actual hardware memory.

Data Structures
3. Block Representation

Each memory block is represented using a **Block** class with the following fields:

- start: Starting address of the block
- size: Size of the block
- free: Boolean flag indicating whether the block is free or allocated
- id: Unique identifier assigned to allocated blocks

Blocks are stored in a list in increasing order of starting address. This structure allows easy traversal for allocation, deallocation, and block coalescing.

4. Allocation Strategies

The simulator implements three dynamic memory allocation strategies:

**First Fit**
The first free block that is large enough to satisfy the request is selected. This is also the default. This strategy is fast but has the risk of external fragmentation when repeatedly used.

**Best Fit**
Among all free blocks that can satisfy the request, the smallest such block is selected. This reduces wasted space but requires scanning all blocks.

**Worst Fit**
The largest available free block is selected for allocation. This attempts to leave larger contiguous free regions but may cause inefficient space usage.

The allocator can be switched at runtime using the CLI command *set_allocator*.

5. Deallocation and Fragmentation Handling

When a block is freed, it is marked as available and adjacent free blocks are merged (coalesced) to reduce external fragmentation.

The simulator tracks:
- Total used memory
- Total free memory
- Largest contiguous free block
- External fragmentation

External fragmentation is computed as:

External Fragmentation = 1 − (Largest Free Block / Total Free Memory)

This allows comparison of allocation strategies under similar workloads.

6. Cache Simulation

The project includes a multilevel CPU cache simulation with two cache levels: L1 and L2.

Each cache level is configurable with:
- Cache size
- Block size
- Associativity
- Replacement policy

Memory accesses generated during allocation are passed through the cache hierarchy to simulate cache hits and misses.

Replacement Policy

FIFO (First-In, First-Out) replacement is implemented. When a cache set is full, the oldest cache line is evicted.

The cache simulation is designed to model access behavior rather than exact hardware timing.

7. Command-Line Interface

The simulator provides an interactive command-line interface with the following commands:

- init <size>: Initialize memory
- malloc <size>: Allocate memory
- free <id>: Free a block
- dump: Display memory layout
- stats: Show memory statistics
- set_allocator <type>: Change allocation strategy
- exit: Exit the simulator

This interface allows users to test different allocation strategies and observe fragmentation effects in real time.

8. Limitations

- The simulator does not model virtual memory or paging.
- Cache timing and latency are not simulated.
- Memory addresses are abstracted as integer offsets.
- The project focuses on conceptual correctness rather than performance optimization.

Despite these limitations, the simulator effectively demonstrates core memory management concepts.

9. Conclusion

This project demonstrates dynamic memory allocation, fragmentation behavior, and cache simulation using user-space abstractions. By implementing multiple allocation strategies and a multilevel cache hierarchy, the simulator provides insight into operating system memory management decisions.

The design prioritizes clarity and modularity, making the system easy to extend with additional features such as paging or alternative cache policies.
