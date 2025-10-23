from stack import Stack


class PostfixEvaluator:
    """Evaluates postfix expressions using a stack."""

    def __init__(self):
        """Initialize the postfix evaluator."""
        self.operators = {'+', '-', '*', '/'}

    def evaluate(self, expression):
        """Evaluate a postfix expression.

        Args:
            expression: A string containing the postfix expression with space-separated tokens.

        Returns:
            The result of evaluating the expression.
        """
        stack = Stack()
        tokens = expression.split()

        for token in tokens:
            if token in self.operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self._apply_operator(operand1, operand2, token)
                stack.push(result)
            else:
                stack.push(float(token))

        return stack.pop()

    def _apply_operator(self, operand1, operand2, operator):
        """Apply an operator to two operands.

        Args:
            operand1: The first operand.
            operand2: The second operand.
            operator: The operator to apply (+, -, *, /).

        Returns:
            The result of applying the operator.
        """
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
