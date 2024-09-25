# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = self.inOrderTraversal(root)
        newTree = self.buildTree(arr)
        return newTree

    
    def inOrderTraversal(self, node):
        if node is None:
            return []
        return self.inOrderTraversal(node.left) + [node.val] + self.inOrderTraversal(node.right)
    

    def buildTree(self, sortedArr):
        if not sortedArr:
            return None
        mid = len(sortedArr) // 2
        root = TreeNode(sortedArr[mid], self.buildTree(sortedArr[:mid]), self.buildTree(sortedArr[mid+1:]))
        return root
        
