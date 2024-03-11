def ShellSort(elements):
    elements = list(set(elements))

    l = []
    size = len(elements)
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            l.append(anchor)
            j = i
            while j>=gap and elements[j - gap] > anchor:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap = gap//2


if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    ShellSort(elements)
    print(elements)