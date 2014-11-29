from unittest import TestCase
from trinary_tree import TrinaryTree


class TrinaryTreeTest(TestCase):
    def _build_common_trinary_tree(self, values):
        tree = TrinaryTree()
        [tree.insert(value) for value in values]
        return tree

    def test_should_insert_properly(self):
        tree = self._build_common_trinary_tree([5, 4, 9, 5, 7, 2, 2])
        expect = "5,4,5,9,2,7,2"
        self.assertEqual(expect, str(tree))

    def test_should_upward_middle_child_given_middle_child_exist(self):
        tree = self._build_common_trinary_tree([5, 4, 9, 5, 7, 2, 2])
        tree.delete(5)
        expect = "5,4,9,2,7,2"
        self.assertEqual(expect, str(tree))

    def test_should_upward_left_child_given_only_left_child_exist(self):
        tree = self._build_common_trinary_tree([5, 4, 9, 7, 2, 2])
        tree.delete(9)
        expect = "5,4,7,2,2"
        self.assertEqual(expect, str(tree))

    def test_should_upward_right_child_given_only_right_child_exist(self):
        tree = self._build_common_trinary_tree([5, 4, 9, 10, 2, 2])
        tree.delete(9)
        expect = "5,4,10,2,2"
        self.assertEqual(expect, str(tree))

    def test_should_upward_right_child_given_both_left_and_right_children_exist(self):
        tree = self._build_common_trinary_tree([5, 4, 9, 4.5, 7, 2, 2])
        tree.delete(5)
        expect = "9,4,2,4.5,2,7"
        self.assertEqual(expect, str(tree))
