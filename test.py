from icecream import ic
from collections import Counter
from typing import List
import string

# def isSubsequence(s: str, t: str) -> bool:
#         i = 0
#         res = 0
#         len_s = len(s)
#         for el in t:
#             if i == len_s:
#                 break
#             ic(el, s[i])
#             if s[i] == el:
#                 res += 1
#                 i += 1
#         return res == len_s


# ic(isSubsequence("abc", "ahbgdc"))



# def findMaxAverage(nums: List[int], k: int) -> float:
#     if not nums:
#         return 0
#     if len(nums) == 1:
#         return nums[0] / k
#     res = []
#     for i in range(len(nums) - k + 1):
#         res.append(sum(nums[i: i+k]) / k)
#     ic(res)
#     return max(res)


# ic(findMaxAverage([1,12,-5,-6,50,3], 4))
# # ic(findMaxAverage([5], 1))
# ic(findMaxAverage([0,1,1,3,3], 4))
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_value(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_value_recursive(self.root, value)

    def _add_value_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_value_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_value_recursive(node.right, value)

    def contains_value(self, value):
        return self._contains_value_recursive(self.root, value)

    def _contains_value_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._contains_value_recursive(node.left, value)
        else:
            return self._contains_value_recursive(node.right, value)

    def remove_value(self, value):
        self.root = self._remove_value_recursive(self.root, value)

    def _remove_value_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove_value_recursive(node.left, value)
        elif value > node.value:
            node.right = self._remove_value_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_value = self._find_min_value(node.right)
                node.value = min_value
                node.right = self._remove_value_recursive(node.right, min_value)
        return node

    def _find_min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value
tree = BinaryTree()

# Добавление значений
tree.add_value(5)
tree.add_value(3)
tree.add_value(7)
tree.add_value(2)
tree.add_value(4)
tree.add_value(6)
tree.add_value(8)
ic(tree.contains_value(7))
ic(tree.contains_value(9))
tree.remove_value(7)
ic(tree.contains_value(7))