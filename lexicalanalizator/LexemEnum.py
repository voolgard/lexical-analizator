from enum import Enum

LexemType = Enum(
    'Type',
    ['EOF', 'OPERATOR', 'STRING', 'CHAR', 'ERROR']
)

LexemToken = Enum(
    'Token',
    ['EOF', 'SEMICOLOM']
)
