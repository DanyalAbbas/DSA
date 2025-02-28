def merge_two_sorted_lists(a,b, elements, key, descending=False):
    len_a = len(a)
    len_b = len(b)
    i ,j, k = 0, 0, 0

    if descending:
        while i < len_a and j < len_b:
            if a[i].get(key) >= b[j].get(key):
                elements[k] = a[i]
                i += 1
            else:
                elements[k] = b[j]
                j += 1
            k += 1
    else:
        while i < len_a and j < len_b:
            if a[i].get(key) <= b[j].get(key):
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


def MergeSort(elements, key, descending=False):
    if len(elements) <= 1:
        return
    mid = len(elements)//2
    left = elements[:mid]
    right = elements[mid:]

    MergeSort(left, key)
    MergeSort(right, key)

    merge_two_sorted_lists(left, right, elements, key, descending)


if __name__ == "__main__":
    a = [5,8,12,56]
    b = [7,9,45,51]
    arr = [5,2,6,763,7325,25,326,3,8]
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    # print(merge_two_sorted_lists(a,b,arr))
    MergeSort(elements, "name")
    print(elements)