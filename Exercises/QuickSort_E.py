def swap(a,b, arr):
    if a != b:
        arr[a] , arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot = elements[end]
    P_index = start

    for i in range(start, end):
        if elements[i] < pivot:  
            swap(i, P_index, elements)
            P_index += 1

    swap(P_index, end, elements)
    return P_index

def QuickSort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        QuickSort(elements, start, pi-1)
        QuickSort(elements, pi+1, end)

if __name__ == "__main__":
    elements = [29,11,9,7,2,28,15]
    QuickSort(elements, 0, len(elements) - 1)
    print(elements)