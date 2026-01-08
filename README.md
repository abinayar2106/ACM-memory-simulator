# Memory Management Simulator

## Overview
This project is a **user-space memory management simulator** that models how an operating system allocates and deallocates memory at runtime. It implements multiple dynamic memory allocation strategies and simulates a **multilevel CPU cache hierarchy** to analyze memory access behavior.

The goal of this project is **not** to build a real OS kernel, but to gain hands-on experience with core **operating system memory-management concepts** using simple and well-defined abstractions.

## Features
- Dynamic memory allocation and deallocation  
- Allocation strategies:
  - First Fit  
  - Best Fit  
  - Worst Fit  
- External fragmentation analysis  
- Memory block splitting and coalescing  
- Multilevel cache simulation (L1 and L2)  
- FIFO cache replacement policy  
- Interactive command-line interface (CLI)  


## Project Structure

```text
memory-simulator/
├─ src/
│  ├─ allocator.py   # Memory allocation logic
│  ├─ cache.py       # Multilevel cache simulation
│  └─ main.py        # CLI and program entry point
├─ docs/
│  └─ design.md      # Design documentation
└─ README.md
```
## How to Run 
### Requirements - Python 3.8 or higher ### Run the Simulator
bash
python src/main.py

### CLI Commands

-init <size> – Initialize memory with the given size  
-malloc <size> – Allocate memory  
-free <block_id> – Free allocated memory  
-dump – Display memory layout  
-stats – Display memory statistics  
- set_allocator <first_fit | best_fit | worst_fit> – Set allocation strategy  
- exit – Exit the simulator  

### Cache Simulation

The simulator models a **two-level cache hierarchy (L1 and L2)**.

Each cache level has configurable:
- Cache size  
- Block size  
- Associativity  

A **FIFO replacement policy** is used when cache sets are full.

Cache **hits and misses** are tracked to analyze memory access patterns.

### Evaluation Metrics

- Used memory  
- Free memory  
- Largest free block  
- External fragmentation  
- Cache hit count  
- Cache miss count  

### Demo Video

A short **2–3 minute demo video** explaining the project design and demonstrating the working simulator.

📎 **Demo Video Link:** *(add link here)*
