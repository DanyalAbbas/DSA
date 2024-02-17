 # ARRAY / LIST 0(n)

stock_prices = []

with open("stock_prices.csv", "r") as f:
    for i in f:
        date, price = i.split(",")
        stock_prices.append([date,float(price)])

# print(stock_prices)

for i in stock_prices:
    if i[0] == "march 9":
        pass
        # print(i[1])

# HASH TABLE / DICTIONARY O(1)

stock_prices_ = {}

with open("stock_prices.csv", "r") as f:
    for i in f:
        date, price = i.split(",")
        stock_prices_[date] = float(price)

# print(stock_prices_)
# print(stock_prices_["march 9"])

# HASH FUNCTION AND TABLE DSA

class HashTable():
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        # print(self.arr)

    def get_hash(self, key):
        h = 0
        for i in key:
            h+= ord(i)
        return h%self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None 




t = HashTable()
t["march 6"] = 300
t["march 1"] = 54
t["march 3"] = 342
t["march 2"] = 877
print(t["march 6"])

print(t.arr)
del t["march 6"]
print(t.arr)
