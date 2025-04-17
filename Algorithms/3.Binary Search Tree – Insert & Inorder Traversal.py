class Node:
    def __init__(self, value: int):
        self.value = value       # Current node's value
        self.left: Node | None = None   # Smaller values go here
        self.right: Node | None = None  # Larger values go here

def insert(root: Node | None, value: int) -> Node:
    """
    Insert a value into the binary search tree.
    """
    if root is None:
        return Node(value)  # If no node exists, create one

    if value < root.value:
        # Insert into left subtree
        root.left = insert(root.left, value)
    else:
        # Insert into right subtree
        root.right = insert(root.right, value)

    return root  # Return root node to preserve tree structure

def inorder_traversal(root: Node | None) -> list[int]:
    """
    Traverse the tree in-order (left → root → right) and return values.
    """
    if root is None:
        return []

    # Recursively collect left, current, and right values
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

values = [5, 3, 7, 1, 4]
root = None

for value in values:
    root = insert(root, value)

print(inorder_traversal(root))
# Output: [1, 3, 4, 5, 7]