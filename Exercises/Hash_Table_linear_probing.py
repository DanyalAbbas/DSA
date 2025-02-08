class HashProbing:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self, key : str) -> int:
        h = 0
        for i in key:
            h+= ord(i)
        return h%self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        if self.arr[h] != None:
            i = h
            while self.arr[i] != None:
                i += 1
            self.arr[i] = (key, val)
        else:
            self.arr[h] = (key, val)

    def __getitem__(self, key):
        h = self.get_hash(key)
        while self.arr[h][0] != key:
            h += 1
        return self.arr[h][1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        while self.arr[h][0] != key:
            h += 1
        del self.arr[h]



if __name__ == "__main__":
    ll = HashProbing()
    ll["march 7"] = 27
    ll["march 16"] = 69
    ll["march 1"] = 23
    ll["march 2"] = 54
    ll["d"] = 65
    print(ll.arr)
    print(ll["march 2"])
    print(ll["e"])

    del ll["march 1"]
    print(ll.arr)
