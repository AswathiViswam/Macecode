def sum_with_right_neighbor(arr):
    result = []
    for i in range(len(arr) - 1):   # go till second last element
        result.append(arr[i] + arr[i+1])
    return result

# Example
arr = [1, 2, 3, 4]
print(sum_with_right_neighbor(arr))  # [3, 5, 7]
