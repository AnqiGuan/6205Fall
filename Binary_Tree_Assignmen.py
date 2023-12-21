import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Q1 Minimum Depth of Binary Tree
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 1
        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return depth
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
        return depth
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# Q2 Count Complete Tree Nodes
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        level = 0
        node = root.left
        while node:  
            level += 1
            node = node.left
        l = 1<<level  
        r = (l<<1)-1  

        while l < r:
            mid = int((r+l+1)/2)  
            node = root
            path = 1<<(level-1)  
            while node and path > 0:
                if mid & path: node = node.right
                else: node = node.left
                path >>= 1  
            if node: l = mid  
            else: r = mid-1  
        return r  
# Time Complexity: O(log2n)
# Space Complexity: O(1)

# Q3 Find leaves of Binary Tree
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root):
            if not root:
                return 0
            l,r = dfs(root.left),dfs(root.right)
            depth = max(l,r)+1
            res[depth].append(root.val)
            return depth

        res = collections.defaultdict(list)
        dfs(root)
        return [v for v in res.values()]
# Time Complexity: O(n)
# Space Complexity: O(n)

# Q4 Find Largest Value in Each Tree Row
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        q, res = deque(), []
        q.append(root)

        if not root:
            return res

        while q:
            maxVal = float('-inf') 
            for i in range(len(q)): # level by level
                node = q.popleft()
                maxVal = max(maxVal, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxVal)
        return res
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# Q5 Leaf-Similar Trees
class Solution:
    def dfs(self, root, res):
        if root is None:
            return
        if root.left is None and root.right is None:
            res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1, res2 = [], []
        self.dfs(root1, res1)
        self.dfs(root2,res2)
        return True if  res1 == res2  else False
# Time Complexity: O(n1 + n2), n1 and n2 represent nodes number of two tree
# Space Complexity: O(n1 + n2)

# Q6 Deepest Leaves Sum
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue, ans = deque([root]), 0
        while queue:
            cur = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                cur += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans = cur
        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)