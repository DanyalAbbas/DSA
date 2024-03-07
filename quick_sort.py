# Hoare Partition
# Lomuto Partition

def swap(a,b, arr):
    if a != b:
        arr[a] , arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start,end, elements)
    
    swap(pivot_index, end, elements)
    
    return end

def QuickSort(elements, start, end):
    if start < end:
        p_index = partition(elements, start, end)
        QuickSort(elements, start, p_index - 1)
        QuickSort(elements, p_index + 1, end)


if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    QuickSort(elements, 0, len(elements) - 1)
    print(elements)