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
