from lexicalanalizator.Reader import Reader
from lexicalanalizator.LexemEnum import LexemType
from lexicalanalizator.LexemEnum import LexemToken
from lexicalanalizator.Exception import LexicalException


class LexicalAnalizator:
    def __init__(self, reader : Reader):
        self.reader = reader
        self.token = ""
        self.type = ""

    def search_char(self):
        int_chars = ""
        if self.reader.viewNextChar() == '#':
            raise LexicalException(f"Error in line -> {self.reader.column} symbol -> {self.reader.row}")
        while self.reader.viewNextChar().isnumeric():
            int_chars += self.reader.read()
        self.token += chr(int(int_chars))

    def getNextLexeme(self):
        self.token = ""
        self.type = ""
        self.reader.clear_temp_buffer()
        char = self.reader.read()
        row = self.reader.row
        column = self.reader.column
        if not char:
            self.type = LexemType.EOF.name
            self.token = LexemToken.EOF.name
            return [str(column),
                    str(row),
                    self.type,
                    self.token,
                    ''.join(self.reader.get_temp_buffer())]
        if char == ';':
            self.type = LexemType.OPERATOR.name
            self.token = LexemToken.SEMICOLOM.name
            return [str(column),
                    str(row),
                    self.type,
                    self.token,
                    ''.join(self.reader.get_temp_buffer())]
        if char == '=':
            self.type = LexemType.OPERATOR.name
            self.token = LexemToken.EQUAL.name
            return [str(column),
                    str(row),
                    self.type,
                    self.token,
                    ''.join(self.reader.get_temp_buffer())]
        if char == '[':
            self.type = LexemType.SEPARATOR.name
            self.token = LexemToken.LBRACE.name
            return [str(column),
                    str(row),
                    self.type,
                    self.token,
                    ''.join(self.reader.get_temp_buffer())]
        if char == ']':
            self.type = LexemType.SEPARATOR.name
            self.token = LexemToken.RBRACE.name
            return [str(column),
                    str(row),
                    self.type,
                    self.token,
                    ''.join(self.reader.get_temp_buffer())]
        if char == '#':
            self.search_char()
            while self.reader.viewNextChar() == '#':
                self.reader.read()
                self.search_char()
            return [str(column),
                    str(row),
                    LexemType.STRING.name if len(self.token) > 1 else LexemType.CHAR.name,
                    self.token,
                    ''.join(self.reader.get_temp_buffer())]
        return char


def getLexemes(buffer):
    result_lexemes = []
    lexical_analizator = LexicalAnalizator(
        Reader(buffer)
    )
    while True:
        lexeme = lexical_analizator.getNextLexeme()
        result_lexemes.append('\t'.join(lexeme).strip())
        if lexeme[2] == 'EOF':
            break
    return '\n'.join(result_lexemes)
