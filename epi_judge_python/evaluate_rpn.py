from test_framework import generic_test
from icecream import ic

ic.disable()


#7:52
# "11,8,10,*,+,7,12,*,+,12,7,*,+,9,14,*,+,17,+"
def evaluate(expression: str) -> int:
    input_list = expression.split(",")
    stack = []
    # ignore error checking
    operations = {"+", "-", "x", "X", "*", "/"}
    mult_operations = {"x", "X", "*"}
    for item in input_list:
        if item in operations:
            b, a = stack.pop(), stack.pop()
            if item == "+":
                stack.append(a + b)
            elif item == "-":
                stack.append(a - b)
            elif item == "/":
                stack.append(a // b)
            elif item in mult_operations:
                stack.append(a * b)
        else:
            stack.append(int(item))
    return stack[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
