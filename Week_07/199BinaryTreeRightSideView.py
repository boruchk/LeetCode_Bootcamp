# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []

        q = []
        levels = []
        result = []

        # Enqueue Root
        q.append(root)
        curr_level = 0

        while q:
            len_q = len(q)
            levels.append([])

            for _ in range(len_q):
                # Add front of queue and remove it from queue
                node = q.pop(0)
                levels[curr_level].append(node.val)

                # Enqueue left child
                if node.left is not None:
                    q.append(node.left)

                # Enqueue right child
                if node.right is not None:
                    q.append(node.right)
            curr_level += 1
        
        # add last element of each level to result
        for i in range(len(levels)):
            level = levels[i]
            result.append(level[len(level)-1])

        return result
        