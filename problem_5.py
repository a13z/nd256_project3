class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point

        output_list = []
        output = []

        if len(self.children) == 0:
            return []

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
        ## Find the Trie node that represents this prefix
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
test_case_solution = []
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