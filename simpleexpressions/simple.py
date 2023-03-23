class ExpressionTree:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def create_tree_lines(self, last=True, depth=0, tree_lines=None):
        if depth != 0:
            prefix = "    " * (depth - 1) + ("└── " if last else "├── ")
            tree_lines.append(prefix + self.operator)
        else:
            tree_lines.append(self.operator)
        if self.left:
            self.left.create_tree_lines(False, depth + 1, tree_lines)
        if self.right:
            self.right.create_tree_lines(True, depth + 1, tree_lines)

    def __str__(self):
        return f"({self.operator} {self.left} {self.right})"


class ExpressionParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def build_tree(self):
        return self.parse_expression()

    def parse_expression(self):
        left = self.parse_term()
        while self.position < len(self.tokens) and self.tokens[self.position] in ['+', '-']:
            operator = self.tokens[self.position]
            self.position += 1
            right = self.parse_term()
            left = ExpressionTree(operator, left, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.position < len(self.tokens) and self.tokens[self.position] in ['*', '/']:
            operator = self.tokens[self.position]
            self.position += 1
            right = self.parse_factor()
            left = ExpressionTree(operator, left, right)
        return left

    def parse_factor(self):
        token = self.tokens[self.position]
        if token.isnumeric() or token.isalpha():
            self.position += 1
            return ExpressionTree(token, None, None)
        elif token == '(':
            self.position += 1
            expression = self.parse_expression()
            self.position += 1  # skip ')'
            return expression
        else:
            raise ValueError(f'Invalid token at position {self.position + 1}: {token}')


def tokenize(expression):
    tokens = []
    current_token = ""
    for char in expression:
        if char in ["+", "-", "*", "/", "(", ")"]:
            if current_token:
                tokens.append(current_token)
            current_token = ""
            tokens.append(char)
        elif char.isspace():
            if current_token:
                tokens.append(current_token)
            current_token = ""
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
    return tokens


if __name__ == "__main__":
    input_expression = input("Enter a mathematical expression: ")
    token_list = tokenize(input_expression)
    parser = ExpressionParser(token_list)
    expression_tree = parser.build_tree()

    tree_lines = []
    expression_tree.create_tree_lines(tree_lines=tree_lines)
    print('\n'.join(tree_lines))
