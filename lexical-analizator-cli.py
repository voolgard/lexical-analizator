import sys
from lexicalanalizator.LexicalAnalizator import getLexemes

if len(sys.argv) > 1:
    print(getLexemes(sys.argv[1].encode('utf-8')))
else:
    print('Argument not found.')
    print('Use: python3 lexical-analizator-cli.py "line"')
