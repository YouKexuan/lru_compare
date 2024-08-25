import time
from functools import lru_cache

fibonacci_3_counter = 0

# Fibonacci function with lru_cache
@lru_cache(maxsize=None)  # Unlimited cache
def fibonacci_with_cache(n):
    if n < 2:
        return n
    return fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)

# Fibonacci function without lru_cache
def fibonacci_without_cache(n):
    global fibonacci_3_counter
    if n == 3:
        fibonacci_3_counter += 1  # Increment the counter when n == 3
    if n < 2:
        return n
    return fibonacci_without_cache(n-1) + fibonacci_without_cache(n-2)

# Test function to compare execution times
def compare_fibonacci(n):
    print(f"Calculating Fibonacci({n}) with and without cache...\n")
    
    # Measure time with cache
    start_time_with_cache = time.time()
    result_with_cache = fibonacci_with_cache(n)
    end_time_with_cache = time.time()
    time_with_cache = end_time_with_cache - start_time_with_cache

    # Print cache stats
    cache_stats = fibonacci_with_cache.cache_info()
    
    # Measure time without cache
    start_time_without_cache = time.time()
    result_without_cache = fibonacci_without_cache(n)
    end_time_without_cache = time.time()
    time_without_cache = end_time_without_cache - start_time_without_cache
    
    # Output results
    print(f"Result with cache: {result_with_cache}")
    print(f"Time with cache: {time_with_cache:.6f} seconds")
    print(f"Cache stats: {cache_stats}")  # Display cache stats
    
    print(f"\nResult without cache: {result_without_cache}")
    print(f"Time without cache: {time_without_cache:.6f} seconds")

# User input for Fibonacci number to calculate
if __name__ == "__main__":
    n = int(input("Enter the Fibonacci number to calculate: "))
    compare_fibonacci(n)
    print(f"fibonacci(3) was calculated {fibonacci_3_counter} times.")
