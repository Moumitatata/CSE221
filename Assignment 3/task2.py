def special_inversion_counter(array):
    def sort_and_count(start, end):
        if end - start <= 1:
            return 0
        middle = (start + end) // 2
        inversions = sort_and_count(start, middle) + sort_and_count(middle, end) 
        squared_right = sorted([array[k] ** 2 for k in range(middle, end)])
        
        for left_idx in range(start, middle):
            low, high = 0, len(squared_right)
            while low < high:
                mid = (low + high) // 2
                if array[left_idx] > squared_right[mid]:
                    low = mid + 1
                else:
                    high = mid
            inversions += low
        
        array[start:end] = sorted(array[start:end])
        return inversions

    return sort_and_count(0, len(array))

# Input section
size = int(input())
values = list(map(int, input().split()))
print(special_inversion_counter(values))




