# Problem 2. Search in a Rotated Sorted Array

To solve this problem in a runtime complexity of O(log n) I decided to use a self balance BST like Red Black Tree.
This type of tree give us a worst Big O for inserting and searching of O(log n)

I have used the Red Black Tree implementation seen in the lesson and extended it.
I extended it by adding an index attribute in the Node class which is the position of the value in the original array
 and by adding a search method to find an element in the tree and returning its index.

Just FYI, I also fixed the rotation methods for the tree when the grandparent needs to be rotated and it is the root 
 node, e.g. This is the method in the lesson, notice that there is no _else_ clause if p is None which if it is root
 the tree gets disconnected:
 
`     def rotate_right(self, node):
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
                p.right = node_moving_up`
                
 It should be:
`     def rotate_right(self, node):
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
        **else:
            self.root = node_moving_up**`
            
 I sent feedback about this in the website but just letting you know.
 
 Runtime complexity for this problem is O(log n) for inserts and search as required by the problem.
 In this problem we are using a Red Black Tree which will grow based on the size of the input list array
 so the space complexity for the tree is O(n)