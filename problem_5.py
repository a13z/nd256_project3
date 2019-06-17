class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        """
        Method that implements recursively a search of all words we have in Trie
        from a node or prefix
        Args:
           suffix(string): string to pass or accumulate the suffixes until we find a word

        Returns:
           output_list(Array): array of all the words found from a node or prefix
        """
        # array to store all the words found
        output_list = []
        # intermediate array to store words
        output = []

        # base case if a node has no children we got to the end and return []
        if len(self.children) == 0:
            return []

        # iterate and traverse the Trie through children dictionary and append the words
        # to output intermediate array and then add output to the final output_list
        for char in self.children:
            output = self.children[char].suffixes(suffix+char)
            if self.children[char].is_word:
                output.append(suffix+char)
            output_list += output

        return output_list

class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root

        for char in word:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        """
         Find the Trie node that represents this prefix

        Args:
           prefix(string): prefix to find in the Trie
        Returns:
           node(Node): if prefix is found in the Trie return the node. If not, return an empty node.
        """
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return TrieNode()

        return node

def test_function(test_case, solution):
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        MyTrie.insert(word)

    output = []

    print("Test case", test_case)
    prefixNode = MyTrie.find(test_case)
    output = prefixNode.suffixes()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_case = 'f'
test_case_solution = ['unction', 'un', 'actory']
test_function(test_case, test_case_solution)

# Test case 2
test_case = 'b'
test_case_solution = []
test_function(test_case, test_case_solution)

# Test case 3
test_case = 'trigg'
test_case_solution = ['er']
test_function(test_case, test_case_solution)

# Test case 4
test_case = 'trig'
test_case_solution = ['ger', 'onometry']
test_function(test_case, test_case_solution)

# Test case 5
test_case = 'anto'
test_case_solution = ['nym']
test_function(test_case, test_case_solution)

# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
#
#
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
#
#
# interact(f, prefix='');