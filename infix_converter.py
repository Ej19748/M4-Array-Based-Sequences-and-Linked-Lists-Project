from stack import Stack


class InfixToPostfixConverter:
    """Converts infix expressions to postfix notation using a stack."""

    def __init__(self):
        """Initialize the infix to postfix converter."""
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def convert(self, expression):
        """Convert an infix expression to postfix notation.

        Args:
            expression: A string containing the infix expression with space-separated tokens.

        Returns:
            A string containing the postfix expression.
        """
        stack = Stack()
        postfix = []
        tokens = expression.split()

        for token in tokens:
            if token == '(':
                stack.push(token)
            elif token == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    postfix.append(stack.pop())
                stack.pop()
            elif token in self.precedence:
                while (not stack.is_empty() and 
                       stack.peek() != '(' and 
                       stack.peek() in self.precedence and
                       self.precedence[stack.peek()] >= self.precedence[token]):
                    postfix.append(stack.pop())
                stack.push(token)
            else:
                postfix.append(token)

        while not stack.is_empty():
            postfix.append(stack.pop())

        return ' '.join(postfix)
