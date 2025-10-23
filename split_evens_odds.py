from single_linked_list import SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):
    """A singly linked list that can split into evens and odds lists."""

    def split(self):
        """Split the list into evens and odds by reassigning node pointers.

        This method manipulates the node pointers to separate even and odd
        integers into two different lists without creating or destroying nodes.
        After this method completes, the original list is empty.

        Returns:
            A tuple of (evens_list, odds_list) where both are SinglyLinkedList objects.
        """
        evens_list = SinglyLinkedList()
        odds_list = SinglyLinkedList()

        if self.head is None:
            return evens_list, odds_list

        evens_tail = None
        odds_tail = None

        current = self.head

        while current is not None:
            next_node = current.next

            if current.data % 2 == 0:
                if evens_list.head is None:
                    evens_list.head = current
                    evens_tail = current
                else:
                    evens_tail.next = current
                    evens_tail = current
                evens_tail.next = None
            else:
                if odds_list.head is None:
                    odds_list.head = current
                    odds_tail = current
                else:
                    odds_tail.next = current
                    odds_tail = current
                odds_tail.next = None

            current = next_node

        self.head = None

        return evens_list, odds_list
