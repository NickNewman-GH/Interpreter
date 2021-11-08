from os import PathLike
from types import resolve_bases
from .tokens import TokenType, Token
from .lexer import Lexer
from .node import Node, Number, BinOp, UnaryOp
import operator

class InterpreterException(Exception):
    pass

class Interpreter():
    
    def interpret(self, tree: Node) -> float:
        return self._visit(tree)

    def _visit(self, node: Node) -> float:
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_binop(node)
        elif isinstance(node, UnaryOp):
            return self._visit_unop(node)
        raise InterpreterException("invalid node")

    def _visit_number(self, node: Node) -> float:
        return float(node.token.value)

    def _visit_unop(self, node: UnaryOp) -> float:
        op = node.op
        if op.type_ == TokenType.MINUS:
            return -self._visit(node.right)
        elif op.type_ == TokenType.PLUS:
            return self._visit(node.right)
        raise InterpreterException("invalid unary operator")

    def _visit_binop(self, node: BinOp) -> float:
        op = node.op
        binop = {TokenType.PLUS: operator.add,
                 TokenType.MINUS: operator.sub,
                 TokenType.DIV: operator.truediv,
                 TokenType.MUL: operator.mul,
                 TokenType.POW: operator.pow}.get(op.type_)
        if binop:
            return binop(self._visit(node.left), self._visit(node.right))
        # if op.type_ == TokenType.PLUS:
        #     return self._visit(node.left) + self._visit(node.right)
        # elif op.type_ == TokenType.MINUS:
        #     return self._visit(node.left) - self._visit(node.right)
        # elif op.type_ == TokenType.MUL:
        #     return self._visit(node.left) * self._visit(node.right)
        # elif op.type_ == TokenType.DIV:
        #     return self._visit(node.left) / self._visit(node.right)
        # elif op.type_ == TokenType.POW:
        #     return self._visit(node.left) ** self._visit(node.right)
        raise InterpreterException("invalid operator")