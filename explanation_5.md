# Problem 5. Autocomplete with Tries

To solve this problem I just implemented the clases and methods required in the notebook provided.

The code is pretty straight forward but I'll comment a few things.
The suffix method in the TrieNode class, traverse all the nodes linked via its children dictionary
until there is no more children recursively. Once we reach the end and we get out of the recursive functions,
 I check if is_word attribute is true and if so, I add all the letters found up to this point to an array.
 
In the Trie class the only thing new is the find method which basically returns the node representing the prefix
given. If the prefix is not found I create an empty node in order to make the suffix method available and therefore
return an empty array. This is done to cover the test case in which the prefix doesn't exist in the Trie.

Runtime complexity to insert and search a word on a Trie is O(n) being n the length of the word we need to insert or 
search. This is because we need to traverse a Trie and therefore, its nodes, as many times as characters a word has.
 
Space complexity is O(n*m) being n the number of characters and m the length of the words these characters create.
