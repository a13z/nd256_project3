class Node(object):
    def __init__(self, value, index, parent, color):
        self.value = value
        self.index = index # index or position of the value in the array
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)

# Helper for finding the node's grandparent
def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

# Helper for finding the node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, 0, None, 'red')

    def __iter__(self):
        yield from self.root.__iter__()

    # Insert a new node providing the value and index in the array and rebalance the node
    def insert(self, new_val, index):
        new_node = self.insert_helper(self.root, new_val, index)
        self.rebalance(new_node)

    # Insert helper to find the right place to insert a node
    def insert_helper(self, current, new_val, index):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val, index)
            else:
                current.right = Node(new_val, index, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val, index)
            else:
                current.left = Node(new_val, index, current, 'red')
                return current.left

    # rebalance a tree based on the Red Black Tree rules
    def rebalance(self, node):
        # Case 1
        if node.parent == None:
            return

        # Case 2
        if node.parent.color == 'black':
            return

        # Case 3
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))

        gp = grandparent(node)
        # Small change, if there is no grandparent, cases 4 and 5
        # won't apply
        if gp == None:
            return

        # Case 4
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        # Case 5
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    def rotate_left(self, node):
        # Save off the parent of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        else:
            self.root = node_moving_up

        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        else:
            self.root = node_moving_up

        node_moving_up.parent = p

    def search(self, node, value):
        """
        Search a value from a Red Black Tree node down and return the node if found.
        If value is not found returns None

        Args:
           node(Node), value(int): node to search from, value to search
        Returns:
           node(Node): node if value is found. None if value is not in the tree.
        """

        if node.value == value:
            return node

        if node.value < value:
            if node.right is not None:
                node = node.right
            else:
                return None
        elif node.value > value:
            if node.left is not None:
                node = node.left
            else:
                return None

        node_found = self.search(node, value)

        return node_found

# Helper to print a tree from a node
def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if len(input_list) < 1:
        return -1

    # create red black tree and initialised with the first element of input_list
    red_black_tree = RedBlackTree(input_list[0])

    # iterate through the rest of the input_list array and insert the elements in the tree
    for index, value in enumerate(input_list[1:], start=1):
        red_black_tree.insert(value, index)

    # search the number in the tree
    node = red_black_tree.search(red_black_tree.root, number)

    if node is None:
        return -1
    else:
        return node.index

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], -1])
test_function([[1, 2, 3, 4, 5, 6, 7], 1])
test_function([[], -1])
