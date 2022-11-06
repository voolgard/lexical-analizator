import sys
from lexicalanalizator.LexicalAnalizator import getLexemes

line = "[[[]]]\n[][]"
print(getLexemes(line.encode('utf-8')))
# if len(sys.argv) > 1:
#     print(getLexemes(sys.argv[1].encode('utf-8')))
# else:
#     print('Argument not found.')
#     print('Use: python3 lexical-analizator-cli.py "line"')
