def BubbleSort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break
        
    return elements



if __name__ == "__main__":
    elements = [5,9,2,1,67,88,34]

    BubbleSort(elements)
    print(elements)
