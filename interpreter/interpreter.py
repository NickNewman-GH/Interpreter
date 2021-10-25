from .tokens import TokenType, Token

class InterpreterException(Exception):
    pass

class Interpreter():
    
    def __init__(self):
        self._pos : int = -1
        self._current_token: Token = None
        self._text: str = ""
        self._current_char: str = None

    def _next_token(self) -> Token:
        while self._current_char != None:
            if self._current_char.isdigit():
                self._forward()
                return Token(TokenType.INTEGER, self._current_char)
            if self._current_char == "+":
                self._forward()
                return Token(TokenType.PLUS, self._current_char)
            if self._current_char == "-":
                self._forward()
                return Token(TokenType.MINUS, self._current_char)
            raise InterpreterException(f"Bad token {self._current_char}")
        return Token(TokenType.EOS, None)

    def _forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._next_token()
        else:
            raise InterpreterException("Invalid token order")

    def _expr(self) -> int:
        self._current_token = self._next_token()
        left = self._current_token
        self._check_token_type(TokenType.INTEGER)
        operator = self._current_token
        if operator.type_ == TokenType.PLUS:
            self._check_token_type(TokenType.PLUS)
        else:
            self._check_token_type(TokenType.MINUS)
        right = self._current_token
        self._check_token_type(TokenType.INTEGER)
        if operator.type_ == TokenType.PLUS:
            return int(left.value) + int(right.value)
        elif operator.type_ == TokenType.MINUS:
            return int(left.value) - int(right.value)
        raise InterpreterException(f"Bad token {operator}")


    def __call__(self, text : str) -> int:
        return self.interpret(text)

    def interpret(self, text : str) -> int:
        self._text = text
        self._pos = -1
        self._forward()
        return self._expr()