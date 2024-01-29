import sys
import pycodestyle
import os


def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)


def calculate_score(total_errors, file_or_directory, max_score=10):
    lines = count_lines(file_or_directory)
    score = max_score - min(total_errors, max_score)
    return max(0, score)


def check_pep8(file_or_directory):
    style = pycodestyle.StyleGuide(quiet=True)
    if os.path.isfile(file_or_directory):
        result = style.check_files([file_or_directory])
    elif os.path.isdir(file_or_directory):
        result = style.check_files([os.path.join(file_or_directory, f)
                                    for f in os.listdir(file_or_directory) if f.endswith('.py')])
    else:
        print(f"Invalid file or directory: {file_or_directory}")
        return

    total_errors = result.total_errors
    if total_errors == 0:
        print("Code complies with PEP 8.")
    else:
        print(f"Code has {total_errors} PEP 8 violations.")

    # Calculate the score
    score = calculate_score(total_errors, file_or_directory)
    print(f"PEP 8 Score: {score}/10")


if __name__ == "__main__":
    file_or_directory = sys.argv[1]
    check_pep8(file_or_directory)
