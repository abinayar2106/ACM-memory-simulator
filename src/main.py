# src/main.py
from allocator import init_memory, allocate, set_allocator, free_block, dump_memory
def main():
    init_memory(1024)
    
    b1 = allocate(100)
    b2 = allocate(200)
    dump_memory()
    
    free_block(b1)
    dump_memory()
    
    free_block(b2)
    dump_memory()

def cli():
    print("Memory Simulator CLI")
    while True:
        cmd = input("> ").strip().split()
        if not cmd:
            continue

        action = cmd[0].lower()

        if action == "init" and len(cmd) == 2:
            init_memory(int(cmd[1]))
        elif action == "malloc" and len(cmd) == 2:
            allocate(int(cmd[1]))
        elif action == "set_allocator" and len(cmd) == 2:
            set_allocator(cmd[1].lower())
        elif action == "free" and len(cmd) == 2:
            free_block(int(cmd[1]))
        elif action == "dump":
            dump_memory()
        elif action == "stats":
            dump_memory()  # stats are included in dump
        elif action == "exit":
            print("Exiting CLI.")
            break
        else:
            print("Unknown command or wrong syntax.")

if __name__ == "__main__":
    cli()
