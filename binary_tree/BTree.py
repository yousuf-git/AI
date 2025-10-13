'''
Written By:             M. Yousuf                                                                   \n
Date:                   Oct 13, 2025                                                                \n
Description:            Implementation of DFS (Iterative + Recursive) and BFS in Binary Tree        \n
'''

from BNode import BNode

class BTree:
    # root: BNode
    # idx = -1

    def __init__(self, nodes):
        self.idx = -1
        self.root = self.buildTree(nodes)

    def buildTree(self, nodes):
        self.idx+=1
        # Base case - if at current index we have None
        if (not nodes[self.idx]):
            return None
        
        # Grabing the current value and create BNode
        root = BNode(nodes[self.idx])
        
        # Now constructing tree in left and right of current Node
        root.left = self.buildTree(nodes)
        root.right = self.buildTree(nodes)
        
        # Returning the current node (for the first recursion level, it will be main root)
        return root
    
    # =============== DFS PreOrder:      root, left, right ===============
    # Recursive
    def recursiveDfs(self, root):
        if (not root):
            return

        print(root.data, end=" ")
        self.dfs(root.left)
        self.dfs(root.right)
    
    # Iterative
    def iterativeDfs(self, root):
        stack = [root]          # Stack with only root in it
        
        # While there is something in stack
        while(stack.__len__() != 0):
        
            # Grabbing the last element from the stack
            node = stack.pop()
            
            print(node.data, end=" ")
            
            # Pushing left and right child of current node into the stack
            if (node.right):
                stack.append(node.right)
            if (node.left):
                stack.append(node.left)
        
    # ===================== BFS =====================
    def bfs(self, root):
        stack = [root]          # Queue with only root in it
        
        # While there is something in stack
        while(stack.__len__() != 0):
        
            # Grabbing the first element always from the queue
            node = stack.pop(0)
            
            print(node.data, end=" ")
            
            # Pushing left and right child of current node into the stack
            if (node.left):
                stack.append(node.left)
            if (node.right):
                stack.append(node.right)
        


tree = BTree([1,2,4,None,None, 5, None, None, 3, 6, None, None, 7, None, None ])
# tree.recursiveDfs(tree.root)
# tree.iterativeDfs(tree.root)
tree.bfs(tree.root)
print()