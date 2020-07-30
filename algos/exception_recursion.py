
class Messenger(Exception):
    def __init__(self, node):
        self.node = node

def df_search(node, key):
    if node == None: return

    if node.key == key:
        messenger = Messenger(node)
        raise messenger

    df_search(node.left, key)
    df_search(node.right, key)

def search(node, key):
    try:
        df_search(node, key)
    except Messenger as m:
        return m.node

