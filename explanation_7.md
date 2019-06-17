# Problem 7. Request Routing in a Web Server with a Trie

To solve this problem, I implemented a Trie according to the boilerplate code provided.

The RouteTrie Node contains a couple of attributes, the handler and a children dictionary:
The handler is returned once the path is found in the RouteTrie.

The path is splitted by `'/'`, i.e. `split('/')` and stored in an array. 
In RouteTrie, in the insert and find methods, I check and expect the first element to be `'' `which is `'/' `and handler 
is not empty. If it is not there it means that the route it is a relative path and therefore I return None since 
it should start with '/'.

If the split path is `['','']` this is how the root request i.e. `'/'` looks like after using `split('/')`

I also check if there are multiple '/' in the path and skip them either for inserting or finding. 
e.g. this` /home/////about/me` is the same as` /home/about/me`

If the previous steps are passed then a traverse the Trie either if it is to insert a route, in which case I add the
handler, or if it is to find a path in which case I return the handler if exists. If it is not found, then it will 
fallback to the not found attribute in the Router.

The runtime complexity is O(1) since the path is stored in a dictionary and the lookup is constant.
The space complexity is O(m*n) being n the number of words which creates the route and m the length of these words.