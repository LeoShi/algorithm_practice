class Node(object):
    def __init__(self, val, left=None, middle=None, right=None):
        self.right = right
        self.middle = middle
        self.left = left
        self.val = val


class TrinaryTree(object):
    def __init__(self):
        self._root = None

    def __str__(self):
        """
        traverse by level
        """
        if self._root:
            queue, result = [self._root], []
            while queue:
                current_node = queue.pop(0)
                result.append(str(current_node.val))
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.middle:
                    queue.append(current_node.middle)
                if current_node.right:
                    queue.append(current_node.right)
            return ','.join(result)
        return ''

    def insert(self, value):
        if not self._root:
            self._root = Node(value)
            return
        current_node = self._root
        while True:
            if value > current_node.val:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    break
            elif value == current_node.val:
                if current_node.middle:
                    current_node = current_node.middle
                else:
                    current_node.middle = Node(value)
                    break
            elif value < current_node.val:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    break

    def delete(self, value):
        if not self._root:
            return False
        current_node, parent_node = self._root, self._root
        while current_node:
            if value > current_node.val:
                parent_node = current_node
                current_node = current_node.right
            elif value < current_node.val:
                parent_node = current_node
                current_node = current_node.left
            elif value == current_node.val:
                self._remove_node(current_node, parent_node)
                return True
        return False

    def _reset_parent_child_node(self, child_node, parent_node, current_value, is_root):
        if is_root:
            self._root = child_node
        if current_value < parent_node.val:
            parent_node.left = child_node
        else:
            parent_node.right = child_node

    def _replace_current_node_with_its_middle_child(self, current_node, parent_node):
        middle_node = current_node.middle
        middle_node.left = current_node.left
        middle_node.right = current_node.right
        self._reset_parent_child_node(middle_node, parent_node, current_node.val, current_node == parent_node)

    def _replace_current_node_with_its_left_child(self, current_node, parent_node):
        left_node = current_node.left
        self._reset_parent_child_node(left_node, parent_node, current_node.val, current_node == parent_node)

    def _replace_current_node_with_its_right_child(self, current_node, parent_node):
        right_node = current_node.right
        self._reset_parent_child_node(right_node, parent_node, current_node.val, current_node == parent_node)

    def _remove_leaf_node(self, current_node, parent_node):
        self._reset_parent_child_node(None, parent_node, current_node.val, current_node == parent_node)

    def _move_right_node_left_branch_into_bottom_of_left_node_right_branch(self, current_node):
        left_node, right_node = current_node.left, current_node.right
        if right_node.left:
            temp_current_node = left_node.right
            parent_temp_current_node = left_node
            while temp_current_node:
                parent_temp_current_node = temp_current_node
                temp_current_node = temp_current_node.right
            parent_temp_current_node.right = right_node.left
        right_node.left = left_node

    def _remove_node(self, current_node, parent_node):
        if current_node.middle:
            self._replace_current_node_with_its_middle_child(current_node, parent_node)
        elif current_node.left and current_node.right is None:
            self._replace_current_node_with_its_left_child(current_node, parent_node)
        elif current_node.right and current_node.left is None:
            self._replace_current_node_with_its_right_child(current_node, parent_node)
        elif current_node.left and current_node.right:
            self._move_right_node_left_branch_into_bottom_of_left_node_right_branch(current_node)
            self._replace_current_node_with_its_right_child(current_node, parent_node)
        else:
            self._remove_leaf_node(current_node, parent_node)
