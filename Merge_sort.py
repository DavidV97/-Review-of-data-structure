class Merge_sort:

    @classmethod
    def mergeSort(cls, head):

        if head is None or head.nextNode is None:
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
            fast = fast.nextNode

        while fast:
            fast = fast.nextNode

            if fast:
                fast = fast.nextNode
                slow = slow.nextNode

        mid = slow.nextNode
        slow.nextNode = None

        return head, mid

    @classmethod
    def mergeLists(cls, l1, l2):

        temp = None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.data <= l2.data:
            temp = l1
            temp.nextNode = cls.mergeLists(l1.nextNode, l2)

        else:
            temp = l2
            temp.nextNode = cls.mergeLists(l1, l2.nextNode)

        return temp
