def InsertionSort(elements : list):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i-1
        while j>=0 and elements[j] > anchor:
            elements[j+1] = elements[j]
            j-=1
        elements[j+1] = anchor


l = []
while True:
    value = float(input())
    # if value == 0: break
    l.append(value)
    if len(l) == 1: 
        print(l[0])
        continue 
    
    InsertionSort(l)
    index = len(l)//2
    if len(l) %2==0:
        median = (l[index] + l[index-1])
        median /= 2
    else:
        median = l[index]
    print(median)


