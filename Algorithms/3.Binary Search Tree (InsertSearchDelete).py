
class Node:
    def __init__(self, value: int):
        self.value = value # Current node's value
        self.left = None # Smaller values go here
        self.right = None # Larger values go here
def insert(root: Node, value: int) -> Node:
    """
        Insert a value into the binary search tree.
        """
    if root is None: # If no node exists, create one
        return Node(value)
    if value < root.value:
        # Insert into left subtree
        root.left = insert(root.left, value)
    else:
        # Insert into right subtree
        root.right = insert(root.right, value)
    return root # Return root node to preserve tree structure

def inorder_traversal(root: Node | None) -> list[int]:
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def search(root: Node, target: int) -> bool:
    if root is None:
        return False
    if root.value == target:
        return True
    elif target < root.value:
        return search(root.left, target)
    else:
        return search(root.right, target)
def delete(root: Node | None, target: int) -> Node | None:
    if root is None:
        return None

    # Find the node to delete
    if target < root.value:
        root.left = delete(root.left, target)
    elif target > root.value:
        root.right = delete(root.right, target)
    else:
        # Found the node to delete

        # Case 1: No children
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Case 3: Two children
        # Find the smallest value in the right subtree (in-order successor)
        successor = root.right
        while successor.left:
            successor = successor.left

        # Replace current node's value with successor's value
        root.value = successor.value

        # Delete the successor node (which is guaranteed to have at most one child)
        root.right = delete(root.right, successor.value)

    # Return the possibly updated root
    return root


# Example usage
values = [10, 5, 15, 3, 7, 12, 18, 4]
root = None
for n in values:
    root = insert(root, n)

print(inorder_traversal(root))
# Output: [3, 4, 5, 7, 10, 12, 15, 18]
print(search(root, 4))  # Output: True
print(search(root, 8))  # Output: False

# Delete a node with two children (10)
root = delete(root, 10)
print(inorder_traversal(root))
# Output: [3, 5, 7, 12, 15, 18]