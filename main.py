from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter
from single_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


def test_postfix_evaluator():
    """Test the PostfixEvaluator with the provided test data."""
    postfix = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]

    evaluator = PostfixEvaluator()

    print("----- Postfix Evaluator -----")
    for expr in postfix:
        result = evaluator.evaluate(expr)
        if result == int(result) and '/' not in expr:
            print(f"[{expr}] = {int(result)}")
        else:
            print(f"[{expr}] = {result}")


def test_infix_converter():
    """Test the InfixToPostfixConverter with the provided test data."""
    infix = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A * B + C / D",
        "( A + B ) * ( C - D )",
        "A + B * C - D / E",
        "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )",
        "A + ( B - C ) * D",
        "( A + B * ( C - D ) ) / E"
    ]

    converter = InfixToPostfixConverter()

    print("----- Infix to Postfix Converter -----")
    for expr in infix:
        postfix = converter.convert(expr)
        print(f"[{expr}] -> [{postfix}]")


def test_singly_linked_list():
    """Test the SinglyLinkedList with the provided test data."""

    print("---- Build a forward list ----")
    forward_list = SinglyLinkedList()
    forward_list.build_list_forward([10, 20, 30, 40, 50])
    print(forward_list.display())

    forward_list.delete_first()
    print(f"Delete the first node: {forward_list.display()}")

    forward_list.delete_last()
    print(f"Delete the last node: {forward_list.display()}")

    forward_list.delete(30)
    print(f"Delete the interior node: {forward_list.display()}")

    print("---- Build a backward list ----")
    backward_list = SinglyLinkedList()
    for value in [10, 20, 30, 40, 50]:
        backward_list.insertAtBeginning(value)
    print(backward_list.display())

    backward_list.delete_first()
    print(f"Delete the first node: {backward_list.display()}")

    backward_list.delete_last()
    print(f"Delete the last node: {backward_list.display()}")

    backward_list.delete(30)
    print(f"Delete the interior node: {backward_list.display()}")

    print("---- Non-recursive reverse print test----")
    reverse_list = SinglyLinkedList()
    reverse_list.build_list_forward([10, 20, 30, 40, 50])
    print(f"Insertion order: {reverse_list.display()}")
    print(f"Reverse order (recursive): {reverse_list.display_reverse_recursive()}")
    print(f"Reverse order (non-recursive): {reverse_list.display_reverse_nr()}")

    print("---- Remove all test ----")
    remove_all_list = SinglyLinkedList()
    remove_all_list.build_list_forward([1, 2, 4, 6, 1, 3, 6])
    print(remove_all_list.display())

    remove_all_list.remove_all(1)
    print(f"Removing 1 and all duplicates: {remove_all_list.display()}")

    remove_all_list.remove_all(6)
    print(f"Removing 6 and all duplicates: {remove_all_list.display()}")


def test_split_evens_odds():
    """Test the SplitEvensOdds functionality."""
    split_list = SplitEvensOdds()
    split_list.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])

    print(split_list.display())

    evens, odds = split_list.split()

    print(evens.display())
    print(odds.display())
    print(split_list.display())


def main():
    """Run all tests."""
    test_postfix_evaluator()
    print()
    test_infix_converter()
    print()
    test_singly_linked_list()
    print()
    test_split_evens_odds()


if __name__ == "__main__":
    main()
