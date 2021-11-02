from .tokens import TokenType, Token
from .lexer import Lexer

class InterpreterException(Exception):
    pass

class Interpreter():
    
    def __init__(self):
        self._current_token: Token = None
        self._lexer = Lexer()

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise InterpreterException("Invalid token order")

    def _expr(self) -> int:
        self._current_token = self._lexer.next()
        left = self._current_token
        self._check_token_type(TokenType.NUMBER)
        operator = self._current_token
        if operator.type_ == TokenType.PLUS:
            self._check_token_type(TokenType.PLUS)
        else:
            self._check_token_type(TokenType.MINUS)
        right = self._current_token
        self._check_token_type(TokenType.NUMBER)
        if operator.type_ == TokenType.PLUS:
            return float(left.value) + float(right.value)
        elif operator.type_ == TokenType.MINUS:
            return float(left.value) - float(right.value)
        raise InterpreterException(f"Bad token {operator}")

    def __call__(self, text : str) -> int:
        return self.interpret(text)

    def interpret(self, text : str) -> int:
        self._lexer.init(text)
        return self._expr()