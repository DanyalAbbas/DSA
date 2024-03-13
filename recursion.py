def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def list_sum(l : list):
    if len(l) == 1:
        return l[0]
    return l[0] + list_sum(l[1:])
    

if __name__ == "__main__":
    print(find_sum(5))
    print(fib(6))
    print(list_sum([1,2,5,7,4]))