
print("\nBinary Search Algorithm")
print("-" * 50 )
print("This function uses the binary search algorithm, which is much faster than linear search.")
print("Time Complexity O(log n)")
print("\033[31mIf the target is found, it returns the index.\033[0m")
print("\033[31mIf the target is not found, it returns -1.\033[0m\n")
print("-" * 50 )
def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1
    while left <= right:
       
        mid = (left + right) 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = [2, 4, 6, 8, 10]

print(binary_search(numbers, 6))
print(binary_search(numbers, 5))
