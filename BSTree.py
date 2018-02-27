from TreeNode import TreeNode


class BSTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def pre_order_traversal(self):
        def pre_order(node):

            if node is None:
                return
            yield node.data
            yield from pre_order(node.left_node)
            yield from pre_order(node.right_node)
        yield from pre_order(self._root)

    def in_order_traversal(self):
        def in_order(node):

            if node is None:
                return
            yield from in_order(node.left_node)
            yield node.data
            yield from in_order(node.right_node)
        yield from in_order(self._root)

    def post_order_traversal(self):
        def post_order(node):

            if node is None:
                return
            yield from post_order(node.left_node)
            yield from post_order(node.right_node)
            yield node.data
        yield from post_order(self._root)

    @property
    def size(self):
        return self._size

    def __contains__(self, data):
        def _contains(node, data):
            return (
                False if node is None else
                _contains(node.left_node, data) if data < node.data else
                _contains(node.right_node, data) if data > node.data else
                True
            )
        return _contains(self._root, data)

    def add(self, data):
        def _insert(node, data):

            if node is None:
                return TreeNode(data)

            elif data == node.data:
                return None

            elif data < node.data:
                node.left_node = _insert(node.left_node, data)

            elif data > node.data:
                node.right_node = _insert(node.right_node, data)
            return node

        self._root = _insert(self._root, data)

        if self._root:
            self._size += 1

        return self._root is not None

    def delete(self, data):
        def _remove(node, data):
            if node.data == data:
                if not (node.left_node and node.right_node):

                    return node.left_node or node.right_node, True

                else:
                    successor, parent = node.right_node, node

                    while successor.left_node:

                        successor, parent = successor.left_node, successor

                    successor.left_node = node.left_node

                    if parent != node:
                        parent.left_node = successor.right_node
                        successor.right_node = node.right_node

                    return successor, True

            elif data < node.data and node.left_node:
                node.left_node, removed = _remove(node.left_node, data)

                return node, removed

            elif data > node.data and node.right_node:
                node.right_node, removed = _remove(node.right_node, data)

                return node, removed

            return node, False

        if self._root is None:
            return False

        self._root, removed = _remove(self._root, data)
        self._size -= int(removed)

        return removed

    def isEmpty(self):
        if self._root is None:
            return True
        else:
            return False

    def __str__(self):
        s = "Arbol vacío"
        count = 0

        if self.size:
            s = "Pre order: ["

            for i in self.pre_order_traversal():
                if count == 0:
                    s += str(i)
                else:
                    s += ", " + str(i)

                count += 1

            s += "] \nIn order: ["
            count = 0

            for x in self.in_order_traversal():
                if count == 0:
                    s += str(x)
                else:
                    s += ", " + str(x)

                count += 1

            s += "] \nPost order: ["
            count = 0

            for y in self.post_order_traversal():
                if count == 0:
                    s += str(y)
                else:
                    s += ", " + str(y)

                count += 1
            s += "]"

            return (s)

        else:
            return (s)
