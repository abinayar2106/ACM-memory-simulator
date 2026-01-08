# Memory Management Simulator

## Overview on the project
This project is a **user-space memory management simulator** that models how an operating system allocates and deallocates memory at runtime. It implements multiple dynamic memory allocation strategies and simulates a **multilevel CPU cache hierarchy** to analyze memory access behavior.

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

## How to Run 
Requirements - Python 3.8 or higher 
**Run the Simulator**
>>python src/main.py

*CLI Commands*
-init <size> – Initialize memory with the given size  
-malloc <size> – Allocate memory  
-free <block_id> – Free allocated memory  
-dump – Display memory layout  
-stats – Display memory statistics  
- set_allocator <first_fit | best_fit | worst_fit> – Set allocation strategy  
- exit – Exit the simulator

## Project Structure
```text
memory-simulator/
├─ src/
│  ├─ allocator.py   #Memory allocation logic
│  ├─ cache.py       #Multilevel cache simulation
│  └─ main.py        #CLI and program entry point
├─ docs/
│  └─ design.md      #Design documentation
└─ README.md
```
Cache Simulation
The simulator models a **two-level cache hierarchy (L1 and L2)**.

Each cache level has configurable:
- Cache size  
- Block size  
- Associativity  

A FIFO replacement policyis used when cache sets are full.

Cache *hits and misses* are tracked to analyze memory access patterns.

Evaluation Metrics

- Used memory  
- Free memory  
- Largest free block  
- External fragmentation  
- Cache hit count  
- Cache miss count  

### Demo Video
here's a short video highlighting the important features the project has to offer
**Demo Video Link:** *(add link here)*

### Report 
here's the **Report of the project** *(add link here)*
