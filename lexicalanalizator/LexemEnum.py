from enum import Enum

LexemType = Enum(
    'Type',
    ['EOF', 'OPERATOR', 'SEPARATOR', 'STRING', 'CHAR', 'ERROR']
)

LexemToken = Enum(
    'Token',
    ['EOF', 'EQUAL', 'LBRACE', 'RBRACE', 'SEMICOLOM']
)
