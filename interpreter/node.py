
from .tokens import Token


class Node:

    def __str__(self):
        return f"{self.__class__.__name__}"

class Number(Node):

    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Number({self.token.value})"

class BinOp(Node):

    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinOp{self.op.value}({self.left}, {self.right})"