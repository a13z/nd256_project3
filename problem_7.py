# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler):
        """
        Method to insert a RouteTrieNode in the RouteTrie

        Args:
           path(string), handler(string): path to add and handler assigned to the path
        """
        node = self.root

        # if path doesn't start with '/' or handler is empty, we return None
        if path[0] != '' or handler == '':
            return None

        # if path contains 2 elements and they are '' this means path is '/'
        # so we return the root.handler because this has been already initialised
        if len(path) == 2 and path[0] == '' and path[1] == '':
            node.handler = handler
            return

        # if path is valid, we iterate it and add it to the RouteTrie
        for single_path in path[1:]:
            # we skip extra '/' in the path if they exist
            if single_path == '':
                break
            # we keep traversing the RouteTrie if we are finding part of the path
            if single_path in node.children:
                node = node.children[single_path]
            # if it doesn't exist we create a new Node and add the path
            else:
                new_node = RouteTrieNode()
                node.children[single_path] = new_node
                node = new_node
        # We finally add the handler to the path
        node.handler = handler


    def find(self, path):
        """
        Method to find a path in a RouteTrie
        Starting at the root, navigate the Trie to find a match for this path
        Return the handler for a match, or None for no match

        Args:
           path(string): path to find in the RouteTrie
        """

        node = self.root

        # if path doesn't start with '/' we return None since it is a relative path
        if path[0] != '':
            return None

        # This means that the path is '/' so we return the handler
        if len(path) == 2 and path[0] == '' and path[1] == '':
            return node.handler

        # if path is valid, we iterate the path from the first '/'
        for single_path in path[1:]:
            # we skip extra '/' in the path if they exist
            if single_path == '':
                break
            # we keep traversing the RouteTrie if we are finding part of the path
            if single_path in node.children:
                node = node.children[single_path]
            else:
                # this means that some part of the path is not found so we return None
                return None
        # Finally, the node is found so we return the handler
        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler=None):
        """
        Method to initialise Router class

        Args:
           handler(string), not_found_handler(string): handler sets the handler for the root node and
           not_found_handler sets the default route when a path is not found
        """

        self.not_found_handler = not_found_handler
        self.trie = RouteTrie(handler)

    def add_handler(self, path, handler):
        """
        Method to add a handler for a path.

        Args:
           path(string), handler(string): add the handler to a path
        """

        path_list = self.split_path(path)
        self.trie.insert(path_list, handler)

    def lookup(self, path):
        """
        Method to lookup a path in the RouteTrie.
        If path is found we return the handler. If not found we return the default
        not_found_handler which was initialised when we created the TrieRoute

        The path works with and without the trailing slash. It provides the handler
        either way if exists

        I think I covered all bonus points ;)

        Args:
           path(string): path to lookup in the RouteTrie
        """

        path_list = self.split_path(path)

        # find the path in the TrieRoute
        found = self.trie.find(path_list)

        # if not found return the default not_found_handler
        if found is None:
            return self.not_found_handler

        return found

    def split_path(self, path):
        """
        Method to split a path into parts using '/' as a separator

        Args:
            path(string): path to split into parts
        Returns:
            (list): list of elements created from splitting path with '/'
        """

        return path.split('/')

def test_function(test_case, solution):

    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route
    router.add_handler("/home/about/you", "about you handler")  # add a route
    print("Test case", test_case)
    output = router.lookup(test_case)

    if output == solution:
        print("Pass")
    else:
        print("Fail")

# Here are some test cases and expected outputs you can use to test your implementation
# Test case 1
test_case = "/"
test_case_solution = 'root handler'
test_function(test_case, test_case_solution)

# Test case 2
test_case = "/home"
test_case_solution = 'not found handler'
test_function(test_case, test_case_solution)

# Test case 3
test_case = "/home/about"
test_case_solution = 'about handler'
test_function(test_case, test_case_solution)

# Test case 4
test_case = "/home/about/"
test_case_solution = 'about handler'
test_function(test_case, test_case_solution)

# Test case 5
test_case = "/home/about/me"
test_case_solution = 'not found handler'
test_function(test_case, test_case_solution)

# Test case 5
test_case = "/home/////about/me"
test_case_solution = 'not found handler'
test_function(test_case, test_case_solution)

# Test case 5
test_case = "/home/about/you"
test_case_solution = 'about you handler'
test_function(test_case, test_case_solution)