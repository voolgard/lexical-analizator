import glob
from simple import *

tests = sorted([f for f in glob.glob("tests/*.in")])
successful_tests = 0
for test in tests:
    try:
        with open(test, 'r') as content:
            tokens = tokenize(str(content.read()))
            parser = ExpressionParser(tokens)
            expression_tree = parser.build_tree()
            tree_lines = []
            expression_tree.create_tree_lines(tree_lines=tree_lines)
            obtained_data = '\n'.join(tree_lines)
        with open(test.replace('.in', '.out'), 'r') as expected_file:
            expected_data = expected_file.read()
        if obtained_data == expected_data:
            print(f"✅ Test: {test.replace('tests/', '')}")
            successful_tests += 1
        else:
            print(f"Error test: {test.replace('tests/', '')}")
    except Exception as e:
        print(f"Error test: {test.replace('tests/', '')}\nMessage: {str(e)}")

print(f"Total: {successful_tests}/{len(tests)}")
