def swap(a,b, arr):
    if a != b:
        arr[a] , arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot = elements[end]

    P_index = start
    while P_index < end:
        while elements[P_index] < pivot:
            P_index += 1
        i = P_index
        while i <= end and elements[i] > pivot:
            i += 1

        if P_index < i: swap(P_index, i, elements)
        if i == end: break    
        
    return P_index

def QuickSort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        QuickSort(elements, pi+1, end)
        QuickSort(elements, start, pi-1)

if __name__ == "__main__":
    elements = [11,9,29,7,2,28,15]
    QuickSort(elements, 0, len(elements) - 1)
    print(elements)