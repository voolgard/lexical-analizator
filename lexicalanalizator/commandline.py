from lexicalanalizator.lex import LexicalAnalyzer

lexer = LexicalAnalyzer()
tokens = lexer.tokenize(input())
print('\n'.join(str(token) for token in tokens))