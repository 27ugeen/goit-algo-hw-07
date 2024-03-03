class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def sum_bst(root):
    if root is None:
        return 0
    return root.key + sum_bst(root.left) + sum_bst(root.right)

# Example usage for BST
bst_root = None
keys = [50, 30, 70, 20, 14, 40, 60, 80]
for key in keys:
    bst_root = insert(bst_root, key)

print("="*42)
print("Sum of all values in BST:", sum_bst(bst_root))
print("="*42)

class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def insert_avl(root, key):
    if root is None:
        return AVLTreeNode(key)
    elif key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    root.height = 1 + max(get_height_avl(root.left), get_height_avl(root.right))
    balance = get_balance_avl(root)

    if balance > 1 and key < root.left.key:
        return rotate_right_avl(root)

    if balance < -1 and key > root.right.key:
        return rotate_left_avl(root)

    if balance > 1 and key > root.left.key:
        root.left = rotate_left_avl(root.left)
        return rotate_right_avl(root)

    if balance < -1 and key < root.right.key:
        root.right = rotate_right_avl(root.right)
        return rotate_left_avl(root)

    return root

def get_height_avl(root):
    if root is None:
        return 0
    return root.height

def get_balance_avl(root):
    if root is None:
        return 0
    return get_height_avl(root.left) - get_height_avl(root.right)

def rotate_right_avl(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(get_height_avl(z.left), get_height_avl(z.right))
    y.height = 1 + max(get_height_avl(y.left), get_height_avl(y.right))

    return y

def rotate_left_avl(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height_avl(z.left), get_height_avl(z.right))
    y.height = 1 + max(get_height_avl(y.left), get_height_avl(y.right))

    return y

def sum_avl(root):
    if root is None:
        return 0
    return root.key + sum_avl(root.left) + sum_avl(root.right)

# Example usage for AVL tree
avl_root = None
keys = [50, 30, 42, 70, 20, 40, 60, 80]
for key in keys:
    avl_root = insert_avl(avl_root, key)

print("Sum of all values in AVL tree:", sum_avl(avl_root))
print("="*42)