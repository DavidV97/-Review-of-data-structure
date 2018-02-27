class Merge_sort:

    @classmethod
    def mergeSort(cls, head):

        if head is None or head.next_node is None:
            return head

        l1, l2 = cls.divideLists(head)
        l1 = cls.mergeSort(l1)
        l2 = cls.mergeSort(l2)
        head = cls.mergeLists(l1, l2)

        return head

    @classmethod
    def divideLists(cls, head):

        slow = head
        fast = head

        if fast:
            fast = fast.next_node

        while fast:
            fast = fast.next_node

            if fast:
                fast = fast.next_node
                slow = slow.next_node

        mid = slow.next_node
        slow.next_node = None

        return head, mid

    @classmethod
    def mergeLists(cls, l1, l2):

        temp_node = None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.data <= l2.data:
            temp_node = l1
            temp_node.next_node = cls.mergeLists(l1.next_node, l2)

        else:
            temp_node = l2
            temp_node.next_node = cls.mergeLists(l1, l2.next_node)

        return temp_node
