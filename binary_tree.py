class BinarySearchTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # adding data in left side
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []

        # visiting the left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visiting right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False 

        if val > self.data:
            # right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False 
        
    def delete_min(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_min(val)
            else:
                return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_min(val)
            else:
                return None
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_min(min_val)
        
        return self

    def delete_max(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_max(val)
            else:
                return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_max(val)
            else:
                return None
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            max_val = self.left.find_max()
            self.data = max_val
            self.right = self.right.delete_max(max_val)

        return self





def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root


if __name__ == "__main__":
    numbers  = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(1))
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    numbers_tree.delete_min(4)
    print(numbers_tree.in_order_traversal())
    # numbers_tree.delete_min(4)
    # print(numbers_tree.in_order_traversal())