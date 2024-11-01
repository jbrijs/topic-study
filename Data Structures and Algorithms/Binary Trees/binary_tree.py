
class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    def insert(self, val):
        
        queue = [self]

        while queue:
            node = queue.pop()

            if not node.left:
               node.left = BinaryTreeNode(val)

            elif not node.right:
                node.right = BinaryTreeNode(val)
                return 
            
            else:
                queue.append(node.left)
                queue.append(node.right)

    
    def preorder_traversal(self):

        res = [] 
        stack = [self]

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)

                if node.right:
                    stack.append(node.right)
                
                if node.left:
                    stack.append(node.left)
        
        print(res)

    
    def inorder_traversal(self):

        res = []
        stack = []

        current = self

        while current or stack:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            res.append(current.val)

            current = current.right

        print(res)


    def postorder_traversal(self):

        res = []
        stack = []
        last_visited = None
        current = self

        while current or stack:
            
            if current:
                stack.append(current)
                current = current.left
            
            else:
                node = stack[-1]

                if node.right and last_visited != node.right:
                    current = node.right

                else:
                    res.append(node.val)
                    last_visited = stack.pop()


        print(res)

    
    def search(self, value):

        stack = [self]

        while stack:
            node = stack.pop()

            if node:
                if node.val == value:
                    return True
                
                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)
        return False
    
    def delete(self, value):
        if not self:
            return None

        if self.left is None and self.right is None:
            if self.val == value:
                return None
            else:
                return self
            
        queue = [self]
        target_node = None
        deepest_node = None
        parent_of_deepest = None

        while queue:
            node = queue.pop(0)

            if node.val == value:
                target_node = node

            if node.left:
                parent_of_deepest = node
                queue.append(node.left)
            
            if node.right:
                parent_of_deepest = node
                queue.append(node.right)

            deepest_node = node

        if target_node:
            target_node.val = deepest_node.val
            
            if parent_of_deepest and parent_of_deepest.left == deepest_node:
                parent_of_deepest.left = None
            elif parent_of_deepest and parent_of_deepest.right == deepest_node:
                parent_of_deepest.right = None

        return self

            

            