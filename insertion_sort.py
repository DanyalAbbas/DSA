def InsertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j  = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor

def InsertionSortinDS(elements):
     for j in range(1,len(elements)):
        i = 0
        while elements[j] > elements[i]:
            i += 1
        m = elements[j]
        for k in range(j-i):
            elements[j-k] = elements[j-k-1]
        elements[i] = m

if __name__ == "__main__":
    elements = [9,11,29,7,2,15,28]
    # InsertionSort(elements)
    InsertionSortinDS(elements)
    print(elements)