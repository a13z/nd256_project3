# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        node = self.root

        if path[0] != '' or handler == '':
            return None

        if len(path) == 2 and path[0] == '' and path[1] == '':
            node.handler = handler
            return

        for single_path in path[1:]:
            if single_path == '':
                break
            if single_path in node.children:
                node = node.children[single_path]
            else:
                new_node = RouteTrieNode()
                node.children[single_path] = new_node
                node = new_node

        node.handler = handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root

        if path[0] != '':
            return None

        if len(path) == 2 and path[0] == '' and path[1] == '':
            return node.handler

        for single_path in path[1:]:
            if single_path == '':
                break
            if single_path in node.children:
                node = node.children[single_path]
            else:
                return None

        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler=None):

    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
        self.not_found_handler = not_found_handler
        self.trie = RouteTrie(handler)

    def add_handler(self, path, handler):

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie

        path_list = self.split_path(path)
        self.trie.insert(path_list, handler)

    def lookup(self, path):

    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler

        path_list = self.split_path(path)
        found = self.trie.find(path_list)

        if found is None:
            return self.not_found_handler

        return found

    def split_path(self, path):
    # you need to split the path into parts for
    # both the add_handler and lookup functions,
    # so it should be placed in a function here

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
test_case_solution = ''
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