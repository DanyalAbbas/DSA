def merge_two_sorted_lists(a,b, elements):
    len_a = len(a)
    len_b = len(b)
    i ,j, k = 0, 0, 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            elements[k] = a[i]
            i += 1
        else:
            elements[k] = b[j]
            j += 1
        k += 1 
    
    while i < len_a:
        elements[k] = a[i]
        i += 1
        k += 1 
    while j < len_b:
        elements[k] = b[j]
        j += 1
        k += 1


def MergeSort(elements):
    if len(elements) <= 1:
        return
    mid = len(elements)//2
    left = elements[:mid]
    right = elements[mid:]

    MergeSort(left)
    MergeSort(right)

    merge_two_sorted_lists(left, right, elements)


if __name__ == "__main__":
    a = [5,8,12,56]
    b = [7,9,45,51]
    arr = [5,2,6,763,7325,25,326,3,8]

    print(merge_two_sorted_lists(a,b,arr))
    MergeSort(arr)
    print(arr)