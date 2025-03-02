def ShellSort(elements):
    div = 2
    size = len(elements)
    gap = size//div

    while gap > 0:
        index_to_del = []
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j>=gap and elements[j - gap] >= anchor:
                if anchor == elements[j-gap]:
                    index_to_del.append(j)
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        
        index_to_del = list(set(index_to_del))
        index_to_del.sort()
        if index_to_del:
            for i in index_to_del[::-1]:
                del elements[i]
        size = len(elements)
        div *= 2
        gap = size//div

    
    
    print(index_to_del)
    

if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    ShellSort(elements)
    print(elements)