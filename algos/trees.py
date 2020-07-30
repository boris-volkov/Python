from random import randint

class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        print(str(self.data))


def traverse(root):
    if root:
        print('preorder: %d' % root.data)
        tree_traversal(root.left)
        print('inorder: %d' % root.data)
        tree_traversal(root.right)
        print('postorder: %d' % root.data)

def random_tree(num_nodes):
    if num_nodes:
        root = BinaryTreeNode(data = randint(1,10))
        root.left = random_tree(num_nodes - 1)
        root.right = random_tree(num_nodes - 1)
        return root

def print_tree(root, ind = 0):
    if root:
        i = ind
        print('   '*i + str(root.data))
        print_tree(root.left, i + 1)
        print_tree(root.right, i + 1)

def has_path_sum(tree, remaining_weight):
    if not tree:
        return False
    if not tree.left and not tree.right:
        return remaining_weight == tree.data
    return has_path_sum(tree.left, remaining_weight - tree.data) or has_path_sum(tree.right, remaining_weight - tree.data)
