from BSTNode import BSTNode


class BSTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def pre_order_traversal(self):
        def pre_order(node):

            if node is None:
                return
            yield node.value
            yield from pre_order(node.left)
            yield from pre_order(node.right)
        yield from pre_order(self._root)

    def in_order_traversal(self):
        def in_order(node):

            if node is None:
                return
            yield from in_order(node.left)
            yield node.value
            yield from in_order(node.right)
        yield from in_order(self._root)

    def post_order_traversal(self):
        def post_order(node):

            if node is None:
                return
            yield from post_order(node.left)
            yield from post_order(node.right)
            yield node.value
        yield from post_order(self._root)

    @property
    def size(self):
        return self._size

    def contains(self, value):
        def _contains(node, value):
            return (
                False if node is None else
                _contains(node.left, value) if value < node.value else
                _contains(node.right, value) if value > node.value else
                True
            )
        return _contains(self._root, value)

    def insert(self, value):
        def _insert(node, value):

            if node is None:
                return BSTNode(value)

            elif value == node.value:
                return None

            elif value < node.value:
                node.left = _insert(node.left, value)

            elif value > node.value:
                node.right = _insert(node.right, value)
            return node

        self._root = _insert(self._root, value)

        if self._root:
            self._size += 1

        return self._root is not None

    def remove(self, value):
        def _remove(node, value):
            if node.value == value:
                if not (node.left and node.right):
                    return node.left or node.right, True

                else:
                    successor, parent = node.right, node

                    while successor.left:
                        successor, parent = successor.left, successor

                    successor.left = node.left

                    if parent != node:
                        parent.left = successor.right
                        successor.right = node.right
                    return successor, True

            elif value < node.value and node.left:
                node.left, removed = _remove(node.left, value)
                return node, removed

            elif value > node.value and node.right:
                node.right, removed = _remove(node.right, value)
                return node, removed

            return node, False

        if self._root is None:
            return False

        self._root, removed = _remove(self._root, value)
        self._size -= int(removed)

        return removed
