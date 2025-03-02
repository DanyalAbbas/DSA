# 1. Write a Python program to calculate the sum of a list of numbers using recursion.

l = [1,2,3,4,5]
def sum_of_list(l):
    if len(l) == 1:
        return l[0]
    return l[-1] + sum_of_list(l[:-1])

print(sum_of_list(l))

# 2. Write a Python program to convert an integer to a string in any base using recursion .



# 3. Write a Python program to sum recursion lists using recursion.
l1 = [1, 2, [3,4], [5,6]]
def sum_list(l : list):
    Summed = 0
    for i in l:
        if type(i) == list:
            Summed += sum_list(i)
        else:
            Summed += i
    return Summed


print(sum_list(l1))