from test_framework import generic_test
from test_framework.test_failure import TestFailure

#824
class Queue:
    # dynamic resizing with insert & append
    # no dynamic shrinking (yet)
    def __init__(self, capacity: int) -> None:
        # TODO - you fill in here.
        self.first = 0
        self.last = capacity - 1
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        return

    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        # cases: trivial, wrap_around, insert
        if self.size() < (self.last - self.first + 1):
            if self.tail <= self.last:
                self.queue[self.tail] = x 
                self.tail += 1
            else:
                self.queue[0] = x 
                self.tail = 1
        else:
            self.queue[self.head:self.head] = [None] * (self.last - self.first + 1)
            self.last += (self.last - self.first + 1)
            self.head += (self.last - self.first + 1)
            self.enqueue(x)
        return

    def dequeue(self) -> int:
        # TODO - you fill in here.
        result = self.queue[self.head]
        if self.head == self.last:
            self.head = 0
        else:
            self.head += 1
        return result

    def size(self) -> int:
        # TODO - you fill in here.
        if self.head <= self.tail:
            return self.tail - self.head
        else:
            return (
                self.last - self.head
                + self.tail)


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
