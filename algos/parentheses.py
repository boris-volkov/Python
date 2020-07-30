class TreeNode:
    def __init__(self, op, cl, string):
        self.op    =  op 
        self.cl    =  cl
        self.string=  string
        self.left  =  None
        self.right =  None

def generateParenthesis(n: int):
        strings = []
        start = TreeNode(1,0,'(')
        def feed(node, target):
            if node.op > node.cl and node.cl < n:
                node.right = TreeNode(node.op, node.cl + 1, node.string + ')')
                feed(node.right, target)
            if node.op >= node.cl and node.op < n:
                node.left = TreeNode(node.op + 1, node.cl, node.string + '(')
                feed(node.left, target)
            if not (node.right or node.left):
                target.append(node.string)
        feed(start, strings)
        return strings


test = generateParenthesis(3)
print(test)
