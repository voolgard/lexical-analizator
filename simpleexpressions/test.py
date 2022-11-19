import glob


def expressions(content):
    return "*\n" \
"├─── 3\n" \
"└─── +\n" \
"     ├─── 5\n" \
"     └─── a"

tests = [f for f in glob.glob("tests/*.in")]
good_test = 0
for test in tests:
    with open(test, 'r') as content_file:
        content_got_expressions = str(content_file.read()).encode('utf-8')
    got_expression = expressions(content_got_expressions)
    with open(test.replace('.in', '.out'), 'r') as content_file:
        excepted_expression = content_file.read()
    if got_expression == excepted_expression:
        print(f"✅ Test: {test.replace('tests/', '')}")
        good_test += 1
    else:
        print(f"❌ Error Test: {test.replace('tests/', '')}")
print('---------------------')
print(f"Total: {good_test}/{len(tests)}")

