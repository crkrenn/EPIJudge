from test_framework import generic_test
from test_framework.test_failure import TestFailure

from icecream import ic
ic.configureOutput(includeContext=True)

def ic(*argv):
    return None

def global_max(*argv):
    return max(*argv)

class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.max_list = []
        ic(self.stack, self.max_list)
        return None

    def empty(self) -> bool:
        ic(self.stack, self.max_list)
        return len(self.stack) == 0

    def max(self) -> int:
        ic(self.stack, self.max_list)
        return self.max_list[-1]

    def pop(self) -> int:
        self.max_list.pop()
        result = self.stack.pop()
        ic(self.stack, self.max_list)
        return result

    def push(self, x: int) -> None:
        if self.empty():
            new_max = x 
        else:
            new_max = global_max(x, self.max_list[-1])
        self.stack.append(x)
        self.max_list.append(new_max)
        ic(self.stack, self.max_list)
        return None

s = Stack()
ic(s.push(-784))
ic(s.pop())
ic(s.push(452))
ic(s.max())
ic(s.pop())
ic(s.push(761))
ic(s.push(402))
ic(s.max())
ic(s.pop())
ic(s.max())
ic(s.pop())


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
