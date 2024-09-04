def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
numbers = [4, 2, 7, 1, 9]
result = linear_search(numbers, 7)

if result != -1:
    print(f"Found target at index {result}")
else:
    print("Target not found")
