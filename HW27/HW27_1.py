class Node:
    """
    A class representing a single node in a Binary Search Tree (BST).
    Each node has a value (data) and references to its left and right children.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Text representation of a node"""
        return f"Node({self.data})"

# 1. SEARCH FUNCTION
def search(root, data):
    """
    Recursive data search in a Binary Search Tree (BST).
    :param root: The current root of the subtree from which the search starts.
    :param data: The value we are looking for.
    :return: The node, if found, or None.
    """

    # Base case 1: Node not found, or we have reached the end of the branch.
    if root is None:
        print(f"Data {data} is not found in this branch.")
        return None
    # Base case 2: Data found
    if root.data == data :
        print (f"Data {data} is founded!")
        return root
    # Recursion logic: We determine where to go next (left or right).
    if data < root.data :
        # Data is smaller than the current data, we go left
        direction = 'left'
        print(f"Compared {data} with {root.data}; go {direction}")
        return search(root.left, data)
    else :
        # Data is bigger than current data, go right
        direction = 'right'
        print(f"Compared {data} with {root.data}: go {direction}")
        return search(root.right, data)

# 2. INSERT FUNCTION
def insert (root, data) :
    """
    Inserts a new data into the BST.
    This function is necessary for correct insertion of the subtree.
    """
    #  Recursion termination condition: We found an empty space (None).
    if root is None :
        # Insertion: Create a new node with a data.
        # Connection: Return this new node to the parent function,
        #  which will assign it to “root.left” or “root.right”.
        return Node(data)
    if data < root.data :
        root.left = insert(root.left, data)
    elif data > root.data :
        root.right = insert(root.right, data)
    # Return the unchanged root back so that the parent nodes know that their
    # structure (except for one branch) remains correct.
    return root

# 3. Subtree Insertion
def inorder_traversal(root, result):
    """
    Helper function: traverses the tree inorder (Left-Root-Right) to get all elements.
    Used to insert a subtree to guarantee the BST order.
    """
    if root:
        inorder_traversal(root.left, result)
        result.append(root.data)
        inorder_traversal(root.right, result)

def insert_subtree(main_root, sub_tree_root):
    """Inserts all nodes “sub_tree_root” into “main_root”"""
    if sub_tree_root is None:
        print("Data of sub_tree is empty.")
        return main_root
    # Get all datas from a subtree
    sub_datas = []
    # sub_tree traversal Inorder
    inorder_traversal(sub_tree_root, sub_datas)
    # insert new data into the main tree
    current_root = main_root
    for data in sub_datas:
        current_root = insert(current_root, data)
        print(f"Insert data: {data}")
    return current_root

# 4. Subtree Removal
def remove_subtree(root, data_to_remove) :
    """
    Removes the node containing “data_to_remove” and its entire subtree.

    :param root: The current root of the subtree.
    :param data_to_remove: The data of the node from which the removal starts.
    :return: Returns the updated root.
    """
    if root is None :
        return None
    if root.data == data_to_remove :
        print(f"Root of the sub-tree found for removal: {data_to_remove}")
        # We return None, which effectively breaks the branch
        return None
    if data_to_remove < root.data:
        # If search(root.left, data) returns None, root.left will be broken
        root.left = remove_subtree(root.left, data_to_remove)
    else :
        root.right = remove_subtree(root.right, data_to_remove)
    return root

# ----------------- EXAMPLES OF USE -----------------
#        8
#      /   \
#     3     10
#    / \     \
#   1   6     14
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
print(f"Main root is : {root.data}")
# search function
print("-"*20)
print("Search function")
result_found = search(root, 6)
if result_found:
    print(f"Founbed: {result_found.data}")
result_found = search(root, 14)
if result_found:
    print(f"Founbed: {result_found.data}")
result_found = search(root, 20)
if result_found:
    print(f"Founbed: {result_found.data}")
# insert function
print("-"*20)
print("Insert function")
insert(root, 7)
insert(root, 12)
print("Datas of main root: ", end="")
root_datas = []
inorder_traversal(root, root_datas)
#        8
#      /   \
#     3     10
#    / \    / \
#   1   6  12   14
#        \
#         7
print(root_datas)
# 1. Створення піддерева для вставки
sub_root = Node(5) # Це корінь піддерева, але його елементи будуть вставлені окремо
insert(sub_root, 9)
insert(sub_root, 11)
print("Datas of sub-tree: ", end="")
sub_datas = []
inorder_traversal(sub_root, sub_datas)
print(sub_datas)
# Inserting a sub-tree into the main tree
root = insert_subtree(root, sub_root)
result_datas = []
inorder_traversal(root, result_datas)
print(f"Main tree after inserting sub-tree: {result_datas}")
#           8
#         /     \
#        3       10
#       / \      / \
#      1   6    9   14
#         / \      /
#        5   7    12
#                 /
#               11

# Remove sub-tree fubction
print("-"*20)
print("Remove function")
data_to_remove = 6
root = remove_subtree(root, data_to_remove)
# Chech datas
final_datas = []
inorder_traversal(root, final_datas)
print(f"Main tree after remove ({data_to_remove}): {final_datas}")
#           8
#         /     \
#        3       10
#       /       / \
#      1       9   14
#                  /
#                12
#               /
#             11

