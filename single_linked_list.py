from stack import Stack


class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        """Initialize a node with data."""
        self.data = data
        self.next = None


class SinglyLinkedList:
    """A singly linked list implementation."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def build_list_forward(self, values):
        """Build a list by inserting values at the end (forward order).

        Args:
            values: A list of values to insert.
        """
        for value in values:
            self.insertAtEnd(value)

    def insertAtEnd(self, data):
        """Insert a node at the end of the list.

        Args:
            data: The data to insert.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def insertAtBeginning(self, data):
        """Insert a node at the beginning of the list.

        Args:
            data: The data to insert.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first node with the given data.

        Args:
            data: The data to delete.

        Returns:
            True if a node was deleted, False otherwise.
        """
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def delete_first(self):
        """Delete the first node in the list."""
        if self.head is not None:
            self.head = self.head.next

    def delete_last(self):
        """Delete the last node in the list."""
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None

    def remove_all(self, data):
        """Remove all nodes with the given data.

        Args:
            data: The data to remove from all nodes.
        """
        while self.head is not None and self.head.data == data:
            self.head = self.head.next

        if self.head is None:
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
            else:
                current = current.next

    def display(self):
        """Display the linked list.

        Returns:
            A string representation of the list.
        """
        if self.head is None:
            return "Head -> None"

        result = "Head"
        current = self.head
        while current is not None:
            result += f" -> {current.data}"
            current = current.next
        result += " -> None"
        return result

    def display_reverse_recursive(self, node=None):
        """Display the list in reverse order using recursion.

        Args:
            node: The current node (defaults to head).

        Returns:
            A string representation of the list in reverse.
        """
        if node is None:
            node = self.head

        if node is None:
            return "None <- Head"

        if node.next is None:
            return f"None <- {node.data} <- Head"

        rest = self.display_reverse_recursive(node.next)
        return f"{rest.replace(' <- Head', '')} <- {node.data} <- Head"

    def display_reverse_nr(self):
        """Display the list in reverse order using a stack (non-recursive).

        Returns:
            A string representation of the list in reverse.
        """
        if self.head is None:
            return "None <- Head"

        stack = Stack()
        current = self.head

        while current is not None:
            stack.push(current.data)
            current = current.next

        result = "None"
        first = True
        while not stack.is_empty():
            if first:
                result += f" <- {stack.pop()}"
                first = False
            else:
                result += f" -> {stack.pop()}"
        result += " <- Head"

        return result

    def is_empty(self):
        """Check if the list is empty.

        Returns:
            True if the list is empty, False otherwise.
        """
        return self.head is None
