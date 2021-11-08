from .tokens import TokenType, Token

class LexerException(Exception):
    pass

class Lexer():
    
    def __init__(self):
        self._pos : int = -1
        self._current_char: str = None
        self._text: str = ""

    def next(self) -> Token:
        while self._current_char != None:
            if self._current_char == " ":
                self._skip()
                continue
            if self._current_char.isdigit():
                return Token(TokenType.NUMBER, self._number())
            if self._current_char == "+":
                char = self._current_char
                self._forward()
                return Token(TokenType.PLUS, char)
            if self._current_char == "-":
                char = self._current_char
                self._forward()
                return Token(TokenType.MINUS, char)
            if self._current_char == "*":
                char = self._current_char
                self._forward()
                return Token(TokenType.MUL, char)
            if self._current_char == "/":
                char = self._current_char
                self._forward()
                return Token(TokenType.DIV, char)
            if self._current_char == "(":
                char = self._current_char
                self._forward()
                return Token(TokenType.LPAREN, char)
            if self._current_char == ")":
                char = self._current_char
                self._forward()
                return Token(TokenType.RPAREN, char)
            raise LexerException(f"Bad token {self._current_char}")
        return Token(TokenType.EOS, None)

    def _forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]
    
    def _skip(self):
        while self._current_char == ' ':
            self._forward()

    def _number(self):
        result: list = []
        left = None
        while self._current_char and (self._current_char.isdigit() or self._current_char == '.'):
            if left:
                if self._current_char == '.' and not left.isdigit():
                    raise LexerException("Wrong number")
                elif not self._current_char.isdigit() and left == '.':
                    raise LexerException("Wrong number")
            result.append(self._current_char)
            left = self._current_char
            self._forward()
        if left == '.':
            raise LexerException("Wrong number")
        return  "".join(result)

    def init(self, text: str):
        self._text = text
        self._pos = -1
        self._forward()