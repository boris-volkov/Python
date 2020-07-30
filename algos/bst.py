import time

class TreeNode(object):
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
    
    def insert(self, key):
        if key == self.val:
            self.count += 1
            return
        if key < self.val:
            if not self.left:
                self.left = TreeNode(key)
                return
            self.left.insert(key)
        else:
            if not self.right:
                self.right = TreeNode(key)
                return
            self.right.insert(key)

five = TreeNode(5)

tree = five
for i in range(10):
    tree.insert(i)

def in_order(root):
    if root == None:
        return

    in_order(root.left)
    print(root.val, root.count)
    time.sleep(0.25)
    in_order(root.right)

def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val, k)
        time.sleep(0.5)
        k -= 1
        print(root.val, k)
        time.sleep(0.5)
        if not k:
            return root.val
        root = root.right


in_order(tree)
print(kth_smallest(tree, 4))

