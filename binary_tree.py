from collections import deque

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        # print("Node object at insert:", TreeNode)   # debug: shows what Node refers to
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.left is None:
                curr.left = new_node
                return
            else:
                queue.append(curr.left)

            if curr.right is None:
                curr.right = new_node
                return
            else:
                queue.append(curr.right)
            
    def display(self):
        if self.root is None:
            return
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            print(curr.value,end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        print()

    def inorder_Traversal(self):
        if self.root is None:
            return
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.left :
                queue.append(curr.left)
            print(curr.value, end=" ")
            if curr.right:
                queue.append(curr.right)

tree = BinaryTree()
tree.insert(23)
tree.insert(30)
tree.insert(20)
tree.insert(10)
tree.inorder_Traversal()

# print(tree.root.left.value)