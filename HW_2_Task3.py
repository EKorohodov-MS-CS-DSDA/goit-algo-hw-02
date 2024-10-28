# Data Structures. Homework 2. Task 3.

ALLOWED_BRACKETS = {'{': '}', '[': ']', '(': ')'}
#test_cases
test_cases = [
    ("( ){[ 1 ]( 1 + 3 )( ){ }}", True),
    ("( 23 ( 2 - 3)", False),
    ("( 11 }", False),
    ("{{():()},{([[}]]", False),
    ("{{():()},{([[],[]])}}", True),
]

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


# just a helper function, don't mind it
def v_print(string:str, verbose:bool=False):
    if verbose:
        print(string)

def is_symmetrical(string:str, verbose:bool=False) -> bool:
    stack = Stack()
    for char in string:
        if char in ALLOWED_BRACKETS:
            stack.push(char)
            v_print(f"Pushed: \"{char}\"", verbose)
        elif char in ALLOWED_BRACKETS.values():
            opening_bracket = stack.pop()
            if not opening_bracket or ALLOWED_BRACKETS[opening_bracket] != char:
                return False
            v_print(f"Popped: \"{opening_bracket}\" because of \"{char}\"", verbose)
        else:
            v_print(f"Skipped: \"{char}\"", verbose)

        v_print(f"Stack: {stack.stack}", verbose)
    return stack.is_empty()


def main():
    for test_case in test_cases:
        string, expected_result = test_case
        result = is_symmetrical(string, True)
        if result == expected_result:
            print(f"Test case '{string}' passed. It is {"not " if not result else ''}symmetrical.")
        else:
            print(f"Test case '{string}' failed. Expected {expected_result}, but got {result}")


if __name__ == '__main__':
    main()
