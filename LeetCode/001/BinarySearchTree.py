from LeetCode.common import TreeNode


class BinarySearchTree:
    def isValidBST(self, root: TreeNode):
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


if __name__ == '__main__':
    num = [2, 1] + [3]
print(num)


# 递归方式
class ValidateBinarySearchTree:
    def __init__(self):
        self.prev = None

    def isValidBST(self, root: TreeNode):
        self.prev = None
        return self.helper(root)

    def helper(self, root: TreeNode):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)
