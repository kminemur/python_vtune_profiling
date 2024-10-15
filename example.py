# example.py
import time

def compute_heavy_operations():
    total = 0
    for i in range(10000000):
        total += i
    return total

def main():
    start_time = time.time()
    result = compute_heavy_operations()
    end_time = time.time()
    print(f"Result: {result}, Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
