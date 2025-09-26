def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # Basic demo
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", numbers)
    sorted_numbers = quicksort(numbers)
    print("Sorted:", sorted_numbers)

    # Search for a number
    index = binary_search(sorted_numbers, 25)
    print(f"Found 25 at index: {index}")

    target = 6
    result = binary_search(sorted_array, target)
    print(f"Searching for {target}: {result} (not found)")

    # Hybrid sort demonstration
    print("\n3. Hybrid Sort Demo:")
    large_numbers = list(range(50, 0, -1))  # [50, 49, ..., 1]
    print(f"Original (first 10): {large_numbers[:10]}")
    hybrid_sort(large_numbers, threshold=5)
    print(f"Sorted (first 10):   {large_numbers[:10]}")

    # Performance benchmark
    print("\n4. Performance Benchmark (100 elements):")
    benchmark_results = benchmark_sorting_algorithms(100)
    for algorithm, time_taken in benchmark_results.items():
        print(f"{algorithm:15}: {time_taken:.6f} seconds")
