class Node(object):
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None

def insert(root, value):

    def insertAt(node):
        if value == node.val:
            return
        if value < node.val:
            if node.left:
                return insertAt(node.left)
            node.left = value
        else:
            if node.right:
                return insertAt(node.right)
            node.right = value

    root = root or Node(value)
    insertAt(root)
    return root

def successorNode(node):
    """ Assuming node has a link to its parent """
    if node.right:
        return successor(node)
    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
    return current.parent

def successor(node):
    """ Assuming it has right child """
    crnt = node.right
    while crnt.left:
        crnt = crnt.left
    return crnt.val

def delete(root, value):
    if not root:
        return None
    if value < root.val:
        root.left = deleteAt(root.left)
    elif value > root.val:
        root.right = deleteAt(root.right)
    else
        if not root.left and not root.right:
            root = None
        elif not root.left or not root.right:
            root = root.left or root.right
        else:
            root.val = successor(root)
            root.right = delete(root.right, root.val)
    return root
