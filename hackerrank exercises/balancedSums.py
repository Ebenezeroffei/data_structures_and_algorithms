def balancedSums(arr):
    left = 0
    right = sum(arr)

    for i in range(len(arr)):
        pivot = arr[i]
        right -= pivot
        if left == right:
            return "YES"
        left += pivot
        
    return "NO"