def find_kth_non_divisible(target_position, divisor):
    if divisor == 1:
        return target_position 
    lower_bound = 1
    upper_bound = 2 * target_position 
    result = 0
    
    while lower_bound <= upper_bound:
        mid_value = (lower_bound + upper_bound) // 2
     
        non_divisible_count = mid_value - (mid_value // divisor)
        
        if non_divisible_count >= target_position:
            result = mid_value
            upper_bound = mid_value - 1  
        else:
            lower_bound = mid_value + 1  
    
    return result

query = int(input())
for i in range(query):
    k, x = map(int, input().split())
    print(find_kth_non_divisible(k, x))