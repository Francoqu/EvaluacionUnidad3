class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self, expression):
        self.expression = expression
        self.root = self.build_tree(self.infix_to_postfix(expression))

    def infix_to_postfix(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()

        for token in tokens:
            if token.isnumeric():
                output.append(token)
            elif token in precedence:
                while (stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()

        while stack:
            output.append(stack.pop())

        return output

    def build_tree(self, postfix):
        stack = []
        for token in postfix:
            if token.isnumeric():
                stack.append(Node(token))
            else:
                node = Node(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack.pop()

    def evaluate(self, node=None):
        if node is None:
            node = self.root

        if node.left is None and node.right is None:
            return int(node.value)

        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        if node.value == '+': return left_val + right_val
        if node.value == '-': return left_val - right_val
        if node.value == '*': return left_val * right_val
        if node.value == '/': return left_val / right_val

    def calculate(self):
        return self.evaluate(self.root)

expression = "3 + 5 * ( 2 - 8 )"
tree = ExpressionTree(expression)
print(f"Resultado de '{expression}':", tree.calculate())
