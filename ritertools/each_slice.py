def iterative(it, size):
    current_slice = []
    for i in it:
        current_slice.append(i)
        if len(current_slice) == size:
            yield current_slice
            current_slice = []
    if current_slice:
        yield current_slice


def recursive(it, size):
    it = iter(it)

    def helper(slice, it):
        # `slice` is the current slice we are building up.
        try:
            el = next(it)
        except StopIteration:
            # If we're at the end of the iterator, and there is a partial slice
            # remaining, yield the partial slice.
            if slice:
                yield slice
            return
        slice = [*slice, el]
        if len(slice) == size:
            yield slice
            yield from helper([], it)
        else:
            yield from helper(slice, it)

    yield from helper([], it)


import unittest
import itertools


class TestEachSlice(unittest.TestCase):
    def helper(self, each_slice):
        # When the last slice is full
        it = range(4)
        out = [list(slice) for slice in each_slice(it, 2)]
        exp = [[0, 1], [2, 3]]
        self.assertEqual(exp, out)

        # When the last slice is not full
        it = range(5)
        out = [list(slice) for slice in each_slice(it, 2)]
        exp = [[0, 1], [2, 3], [4]]
        self.assertEqual(exp, out)

    def test_iterative(self):
        self.helper(iterative)

    def test_recursive(self):
        self.helper(recursive)

