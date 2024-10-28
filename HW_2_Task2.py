# Data Structures. Homework 2. Task 2.
from collections import deque

test_cases = [
    ("11211", True),
    ("abba", True),
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("raCecaR", True),
    ("A Santa at NASA", True),
    ("Not a palindrome", False),
    ("Was it a Car or a cat I saw", True),
]

def is_palindrome(string:str, ignore_whitespaces:bool=True) -> bool:
    if len(string) == 0:
        # consider an empty string to be a palindrome
        return True

    # ignore letter case
    string = string.lower()

    # if set, ignore whitespaces
    if ignore_whitespaces:
        string = ''.join([char for char in string if char != ' '])

    queue = deque(string)
    for _ in range(len(string)//2):
        if queue.popleft() != queue.pop():
            return False
    return True

def main():
    for test_case in test_cases:
        string, expected_result = test_case
        result = is_palindrome(string)
        if result == expected_result:
            print(f"Test case '{string}' passed. It is {"not " if not result else ''}a palindrome.")
        else:
            print(f"Test case '{string}' failed. Expected {expected_result}, but got {result}")

if __name__ == '__main__':
    main()