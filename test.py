import glob
from lexicalanalizator.LexicalAnalizator import getLexemes

tests = [f for f in glob.glob("tests/*.in")]
good_test = 0
for test in tests:
    with open(test, 'r') as content_file:
        content_got_lexeme_bytes = str(content_file.read()).encode('utf-8')
    got_lexeme = getLexemes(content_got_lexeme_bytes)
    with open(test.replace('.in', '.out'), 'r') as content_file:
        excepted_lexeme = content_file.read()
    if got_lexeme == excepted_lexeme:
        print(f"✅ Test: {test.replace('tests/', '')}")
        good_test += 1
    else:
        print(f"❌ Error Test: {test.replace('tests/', '')}")
print('---------------------')
print(f"Total: {good_test}/{len(tests)}")

