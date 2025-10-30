class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def __repr__(self):
        return f"Node {self.value}"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = TreeNode(data)

        else :
            self.recursive_add(self.root , data)

    def recursive_add(self, current_node , value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
                return
            else :
                self.recursive_add(current_node.left , value)

        elif value > current_node.value:
            if current_node.right is None :
                current_node.right = TreeNode(value)
                return
            else :
                self.recursive_add(current_node.right, value)

    def inorder_traversal(self , node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value , end = " ")
            self.inorder_traversal(node.right)

    
    def search(self, node, value):
        if value == node.value :
            return f"{value} is found"
         
        if value < node.value :
            if node.left :
                self.search(node.left , value)
            else :
                print('value not found')

        elif value > node.value :
            if node.right :
                self.search(node.right, value)
            else :
                print(f"{value} not found")
                
    def delete(self, node, data):

        # 1. Base Case: If the node is None, the data is not in the tree.
        # Return None so the parent's link doesn't change.
        if node is None:
            return node  # Or return None, they are equivalent here

        # 2. Recurse down the tree
        if data < node.value:
            # Go left and update the left child
            node.left = self.delete(node.left, data)
        elif data > node.value:
            # Go right and update the right child
            node.right = self.delete(node.right, data)

        # 3. Node found: This is the node to be deleted
        else:
            # Case 1: Node with only one child or no child
            if node.left is None:
                # Return the right child (it might be None)
                return node.right
            elif node.right is None:
                # Return the left child
                return node.left

            # Case 2: Node with two children
            # Get the in-order successor (smallest in the right subtree)
            temp = node.right
            while temp.left:
                temp = temp.left
            
            # print(temp.value) # Your debug print is fine here

            # Copy the successor's value to this node
            node.value = temp.value

            # Delete the in-order successor from the right subtree
            node.right = self.delete(node.right, temp.value)

        # Return the (possibly modified) node to the parent
        return node
    
    # This is the public method users will call
    def delete_data(self, data):
        self.root = self.delete(self.root, data)
        

    def count_nodes(self , node):
        if node is None:
            return 0
        else :
            return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
        
    def height(self, node):
        if node is None:
            return -1
        else :
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return 1 + max(left_height , right_height)
        
    def validate_bst(self):
        def helper(node , min_val, max_val):
            if node is None :
                return True
            
            if node.value <= min_val or node.value >= max_val:
                return False
            
            return (helper( node.left , min_val , node.value) and helper(node.right, node.value , max_val))
        return helper(self.root , float('-inf'), float('inf'))
    
    def get_min(self,node):
        if node is None:
            node = self.root
        
        while node.left :
            node = node.left
        return node.value

    def get_max(self,node):
        if node is None:
            node = self.root
        
        while node.right :
            node = node.right
        return node.value
    

    def sec_min(self,node):
        if node is None :
            node = self.root
        prev = None
        current = node
        while current.left :
            prev = current
            current = current.left
        if current.right:
            return self.get_min(current.right)
        return prev.value
    
    
    
    def closeset_value(self,target):
        def helper(node , closest , target):
            if node is None :
                return closest
            
            if abs(node.value - target) <= abs(closest - target):
                closest = node.value

            if target < node.value:
                return helper(node.left , closest, target)
            elif target > node.value: 
                return helper(node.right, closest, target)
            else :
                return closest
        return helper(self.root , self.root.value, target)
    
    def find_kth_largest(self,k):
        s_list = []

        def inorder(node):

            if node is None:
                return None
            
            inorder(node.left)
            s_list.append(node.value)
            inorder(node.right)

        inorder(self.root)


        if k > 0 and k < len(s_list):
            return s_list[-k]
        else:
            return f'in sufficient position : {k}'
        
    def is_balnced(self):

        return self.get_height_and_check_balance(self.root) != -1

    def get_height_and_check_balance(self, node):
        """
        Helper function that returns:
        - The node's height if it's balanced.
        - -1 if it's unbalanced.
        """
        # Base case: An empty node has height 0 and is balanced.
        if node is None:
            return 0
        
        # 1. Check left subtree
        left_height = self.get_height_and_check_balance(node.left)
        # If the left subtree is unbalanced, pass the -1 signal up
        if left_height == -1:
            return -1
            
        # 2. Check right subtree
        right_height = self.get_height_and_check_balance(node.right)
        # If the right subtree is unbalanced, pass the -1 signal up
        if right_height == -1:
            return -1
            
        # 3. Check current node's balance
        if abs(left_height - right_height) > 1:
            return -1  # This node is unbalanced
        
        # 4. If all good, return the actual height
        return 1 + max(left_height, right_height)

Tree1 = BST()
arr = [4 , 40, 44, 20]
for i in arr:
    Tree1.insert(i)

display = Tree1.inorder_traversal(Tree1.root)
# Tree1.delete_data(4)
print()
print("After Deletion")
display = Tree1.inorder_traversal(Tree1.root)
print()

# res = Tree1.find_kth_largest(2)
# print(res)

print(Tree1.is_balnced())