"""Simple calculator using stacks.

Evaluates infix expressions with + - * / ^ and parentheses, using two stacks:
one for operands (numbers) and one for operators.
"""

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
RIGHT_ASSOCIATIVE = {"^"}


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise ValueError("Invalid expression")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if self._items else None

    def is_empty(self):
        return not self._items


def apply_operator(operands, op):
    b = operands.pop()
    a = operands.pop()
    if op == "+":
        operands.push(a + b)
    elif op == "-":
        operands.push(a - b)
    elif op == "*":
        operands.push(a * b)
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        operands.push(a / b)
    elif op == "^":
        operands.push(a ** b)


def evaluate(expression):
    operands = Stack()
    operators = Stack()
    i = 0
    n = len(expression)
    expect_operand = True  # True at start, after '(' or after an operator

    while i < n:
        ch = expression[i]

        if ch.isspace():
            i += 1
            continue

        # Number (supports decimals)
        if ch.isdigit() or ch == ".":
            j = i
            while j < n and (expression[j].isdigit() or expression[j] == "."):
                j += 1
            operands.push(float(expression[i:j]))
            i = j
            expect_operand = False
            continue

        if ch == "(":
            operators.push(ch)
            expect_operand = True
        elif ch == ")":
            while operators.peek() not in (None, "("):
                apply_operator(operands, operators.pop())
            if operators.peek() != "(":
                raise ValueError("Mismatched parentheses")
            operators.pop()
            expect_operand = False
        elif ch in PRECEDENCE:
            if expect_operand:
                if ch == "-":
                    # Unary minus: treat as 0 - x (no popping needed)
                    operands.push(0.0)
                    operators.push(ch)
                    i += 1
                    continue
                raise ValueError(f"Unexpected operator '{ch}'")
            while True:
                top = operators.peek()
                if top is None or top == "(":
                    break
                if PRECEDENCE[top] > PRECEDENCE[ch] or (
                    PRECEDENCE[top] == PRECEDENCE[ch] and ch not in RIGHT_ASSOCIATIVE
                ):
                    apply_operator(operands, operators.pop())
                else:
                    break
            operators.push(ch)
            expect_operand = True
        else:
            raise ValueError(f"Invalid character '{ch}'")
        i += 1

    while not operators.is_empty():
        op = operators.pop()
        if op == "(":
            raise ValueError("Mismatched parentheses")
        apply_operator(operands, op)

    result = operands.pop()
    if not operands.is_empty():
        raise ValueError("Invalid expression")
    return result


def main():
    print("Stack Calculator (type 'q' to quit)")
    print("Supports + - * / ^ and parentheses, e.g. 3 + 4 * (2 - 1)")
    while True:
        try:
            line = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if line.lower() in ("q", "quit", "exit"):
            break
        if not line:
            continue
        try:
            result = evaluate(line)
            print(int(result) if result == int(result) else result)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
    print("thanks buddy")