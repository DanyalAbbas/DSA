def linear_search(numbers_list, number_to_find):
    for pos, i in enumerate(numbers_list):
        if i == number_to_find:
            return pos
    return -1

def binary_search(numbers_list, number_to_find):
    start = 0
    end = len(numbers_list) - 1
    mid = 0
    
    while start <= end:
        mid = (start + end) // 2
        mid_num = numbers_list[mid]

        if mid_num == number_to_find:
            return mid
        
        if mid_num < number_to_find:
            start = mid + 1
        else:
            end = mid - 1 

    return -1

def binary_search_recursive(numbers_list, number_to_find, start, end):
    if end < start:
        return -1
    
    mid = (start + end) // 2
    mid_num = numbers_list[mid]
    if mid_num == number_to_find:
        return mid
    
    if mid_num < number_to_find:
        start = mid + 1
    else:
        end = mid - 1 

    return binary_search_recursive(numbers_list, number_to_find, start, end)




if __name__ == "__main__":
    numbers_list = [12,15,17,21,26,31,38]
    number_to_find = 31

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f"Number found at {index} using binary search")