class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level


    def print_tree(self, level : int):
        if self.get_level() <= level:
            spaces = "   " * self.get_level()
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if len(self.children):
                for child in self.children:
                    child.print_tree(level)


def build_location_tree():
    root = TreeNode("Global")


    india = TreeNode("india")
    india.add_child(TreeNode("gujarat"))
    india.add_child(TreeNode("dehli"))
    india.add_child(TreeNode("mumbai"))

    pakistan = TreeNode("pakistan")
    pakistan.add_child(TreeNode("karachi"))
    pakistan.add_child(TreeNode("lahore"))

    usa = TreeNode("USA")
    usa.add_child(TreeNode("california"))
    usa.add_child(TreeNode("los angeles"))

    root.add_child(india)
    root.add_child(pakistan)
    root.add_child(usa)

    return root



if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(2)