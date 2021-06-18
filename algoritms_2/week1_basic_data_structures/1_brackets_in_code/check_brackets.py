# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next,i+1))

        if next in ")]}":
            if(not opening_brackets_stack):
                print(i+1)
                return
            elif( are_matching(opening_brackets_stack[-1][0], next)):
                opening_brackets_stack.pop()
            else:
                print(i+1)
                return
    if (not opening_brackets_stack):
        print('Success')
    else:
        print(opening_brackets_stack[0][1])
def main():
    text = input()
    mismatch = find_mismatch(text)



if __name__ == "__main__":
    main()
