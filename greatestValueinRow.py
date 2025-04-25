from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: BFS (Level-order traversal)
# Traverse the tree level-by-level and find the max value at each level.
# TC: O(N) — visit each node once
# SC: O(W) — queue holds nodes up to the max width of the tree


class SolutionBFS:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])  # Start with root in queue

        while queue:
            level_size = len(queue)
            max_val = float("-inf")  # Track max for this level

            for _ in range(level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)  # Update max value

                # Add children to queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_val)  # Add largest value for this level

        return result


# Approach 2: DFS (Preorder with level tracking)
# Recursively track the max value per level by depth.
# TC: O(N) — visit each node once
# SC: O(H) — recursion stack depth (H = height of tree)


class SolutionDFS:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level):
            if not node:
                return

            # First time at this level
            if level == len(res):
                res.append(node.val)
            else:
                res[level] = max(res[level], node.val)  # Update level max

            # Recurse to left and right child
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res


# Tree structure:
#         1
#        / \
#       3   2
#      / \   \
#     5   3   9

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

bfs_sol = SolutionBFS()
dfs_sol = SolutionDFS()

print("Largest values (BFS):", bfs_sol.largestValues(root))
print("Largest values (DFS):", dfs_sol.largestValues(root))
