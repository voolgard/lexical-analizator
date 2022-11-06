from lexicalanalizator.Reader import Reader
from lexicalanalizator.LexemEnum import LexemType
from lexicalanalizator.LexemEnum import LexemToken


class LexicalAnalizator:
    def __init__(self, reader : Reader):
        self.reader = reader
        self.token = ""
        self.type = ""

    def search_char(self):
        int_chars = ""
        while self.reader.viewNextChar().isnumeric():
            int_chars += self.reader.read()
        self.type = LexemType.CHAR.name
        self.token = chr(int(int_chars))

    def getNextLexeme(self):
        self.reader.clear_temp_buffer()
        char = self.reader.read()
        if not char:
            self.type = LexemType.EOF.name
            self.token = LexemToken.EOF.name
            return [str(self.reader.column),
                    str(self.reader.row),
                    self.type,
                    self.token,
                    ''.join(self.reader.get_temp_buffer())]
        if char == ';':
            self.type = LexemType.OPERATOR.name
            self.token = LexemToken.SEMICOLOM.name
            return [str(self.reader.column),
                    str(self.reader.row),
                    self.type,
                    self.token,
                    ''.join(self.reader.get_temp_buffer())]
        if char == '#':
            self.search_char()
            return [str(self.reader.column),
                    str(self.reader.row),
                    self.type,
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
