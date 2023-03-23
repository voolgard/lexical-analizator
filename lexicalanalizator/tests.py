import glob
from lexicalanalizator.lex import LexicalAnalyzer

test_files = sorted(
    [
        f for f in glob.glob("tests/*.in")
    ]
)
successful_tests = 0
for test_file in test_files:
    lex_analyzer = LexicalAnalyzer()
    try:
        with open(test_file.replace('.in', '.out'), 'r') as exp_file:
            expected_output = exp_file.read()
        with open(test_file, 'r') as input_file:
            produced_output = '\n'.join(str(t) for t in lex_analyzer.tokenize(text=str(input_file.read())))
        if produced_output == expected_output:
            print(f"✅ Test: {test_file.replace('tests/', '')}")
            successful_tests += 1
        else:
            print(produced_output)
            print(f"🔴 Error test: {test_file.replace('tests/', '')}")
    except Exception as err:
        if expected_output.strip() == str(err).strip():
            print(f"✅ Test: {test_file.replace('tests/', '')}")
            successful_tests += 1
        else:
            print(f"Error test: {test_file.replace('tests/', '')}\nMessage: {str(err)}")

print(f"Total: {successful_tests}/{len(test_files)}")