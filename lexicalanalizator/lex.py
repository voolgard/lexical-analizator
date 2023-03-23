from dataclasses import dataclass
from enum import Enum


class TokenKind(Enum):
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    INTEGER = 'INTEGER'
    DOUBLE = 'DOUBLE'
    CHAR = 'CHAR'
    STRING = 'STRING'
    OPERATOR = 'OPERATOR'
    SEPARATOR = 'SEPARATOR'
    COMMENT = 'COMMENT'
    END_OF_FILE = 'END_OF_FILE'


class Lexeme(Enum):
    INTEGER = 'INTEGER'
    IDENTIFIER = 'IDENTIFIER'
    SEMICOLON = ';'
    COLON = ':'
    COMMA = ','
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    LEFT_PAREN = '('
    RIGHT_PAREN = ')'

    KEYWORD = 'KEYWORD'
    PROGRAM = 'program'
    VARIABLE = 'var'
    START = 'begin'
    FINISH = 'end'
    ASSIGNMENT = ':='
    PERIOD = '.'
    PROCEDURE = 'procedure'
    FUNCTION = 'function'

    @classmethod
    def is_keyword(cls, value: str) -> bool:
        start_keyword = cls.KEYWORD.name
        end_keyword = cls.FUNCTION.name
        members = cls.__members__
        keys = list(members.keys())
        keywords = keys[keys.index(start_keyword) : keys.index(end_keyword) + 1]
        return any(
            members[e].value == value
            for e in keywords
        )


@dataclass
class Token:
    kind: TokenKind
    lexeme: Lexeme
    value: str
    position: tuple

    def __repr__(self):
        return f"{self.position[0]}\t{self.position[1] + 1}\t{self.kind.value}\t{self.value}\t{self.value}".strip()


class LexicalAnalyzer:
    def __init__(self):
        self.source = None
        self.position = 0
        self.current_char = None
        self.line = 1
        self.column = 0
        self.lexeme_dict = {
            ';': Lexeme.SEMICOLON,
            ':': Lexeme.COLON,
            ',': Lexeme.COMMA,
            '+': Lexeme.PLUS,
            '-': Lexeme.MINUS,
            '*': Lexeme.MULTIPLY,
            '/': Lexeme.DIVIDE,
            '(': Lexeme.LEFT_PAREN,
            ')': Lexeme.RIGHT_PAREN,
            ':=': Lexeme.ASSIGNMENT,
        }

    def peek_next_char(self):
        peek_position = self.position + 1
        if peek_position > len(self.source) - 1:
            return None
        else:
            return self.source[peek_position]

    def raise_error(self):
        raise Exception(f'Invalid character at position {self.position}')

    def move_forward(self):
        self.position += 1
        self.column += 1
        if self.position > len(self.source) - 1:
            self.current_char = None
        else:
            self.current_char = self.source[self.position]

    def skip_whitespace_and_newlines(self):
        while self.current_char is not None and self.current_char.isspace() and self.current_char != '\n':
            self.move_forward()
        if self.current_char == '\n':
            self.line += 1
            self.column = -1
            self.move_forward()

    def process_integer(self):
        start_col = self.column
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.move_forward()
        return Token(kind=TokenKind.INTEGER,
                     lexeme=Lexeme.INTEGER,
                     value=int(result),
                     position=(self.line, start_col))

    def process_identifier(self):
        start_col = self.column
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.move_forward()
        if Lexeme.is_keyword(result):
            return Token(kind=TokenKind.KEYWORD, lexeme=Lexeme(result), value=result, position=(self.line, start_col))
        else:
            return Token(kind=TokenKind.IDENTIFIER, lexeme=Lexeme.IDENTIFIER, value=result,
                         position=(self.line, start_col))

    def retrieve_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace_and_newlines()
                continue

            if self.current_char.isalpha():
                return self.process_identifier()

            if self.current_char.isdigit():
                return self.process_integer()

            if self.current_char == ':' and self.peek_next_char() == '=':
                start_col = self.column
                self.move_forward()
                self.move_forward()
                return Token(kind=TokenKind.OPERATOR, lexeme=Lexeme.ASSIGNMENT, value=':=',
                             position=(self.line, start_col))

            if self.current_char in self.lexeme_dict:
                lexeme_type = self.lexeme_dict[self.current_char]
                start_col = self.column
                self.move_forward()
                return Token(kind=TokenKind.OPERATOR, lexeme=lexeme_type, value=lexeme_type.value,
                             position=(self.line, start_col))

            if self.current_char == '.':
                start_col = self.column
                self.move_forward()
                return Token(kind=TokenKind.OPERATOR, lexeme=Lexeme.PERIOD, value='.', position=(self.line, start_col))

            self.raise_error()

    def tokenize(self, text):
        self.source = text
        self.position = 0
        self.column = 0
        self.current_char = self.source[self.position] if self.source else None
        tokens = []
        while self.current_char is not None:
            token = self.retrieve_next_token()
            tokens.append(token)
        return tokens