class Stack:
  """A stack implementation using Python list."""

  def __init__(self):
      """Initialize an empty stack."""
      self._items = []

  def push(self, item):
      """Add an item to the top of the stack."""
      self._items.append(item)

  def pop(self):
      """Remove and return the top item from the stack.

      Returns:
          The item at the top of the stack.

      Raises:
          IndexError: If the stack is empty.
      """
      if self.is_empty():
          raise IndexError("Cannot pop from an empty stack")
      return self._items.pop()

  def peek(self):
      """Return the top item without removing it.

      Returns:
          The item at the top of the stack.

      Raises:
          IndexError: If the stack is empty.
      """
      if self.is_empty():
          raise IndexError("Cannot peek at an empty stack")
      return self._items[-1]

  def is_empty(self):
      """Check if the stack is empty.

      Returns:
          True if the stack is empty, False otherwise.
      """
      return len(self._items) == 0

  def size(self):
      """Return the number of items in the stack.

      Returns:
          The number of items in the stack.
      """
      return len(self._items)

  def clear(self):
      """Remove all items from the stack."""
      self._items = []

  def __str__(self):
      """Return a string representation of the stack."""
      return f"Stack({self._items})"

  def __repr__(self):
      """Return a string representation of the stack."""
      return self.__str__()
