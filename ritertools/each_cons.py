def iterative(it, size):
    conses = []
    for el in it:
        conses.append([])
        for index, cons in enumerate(conses):
            cons.append(el)
        # print(el, "--", conses)
        if len(conses[0]) == size:
            yield conses.pop(0)


def recursive(it, size):
    it = iter(it)

    def helper(conses, it):
        conses = [*conses, []]
        el = next(it)
        for index, cons in enumerate(conses):
            cons.append(el)
        # print(el, "--", conses)
        if len(conses[0]) == size:
            head, *tail = conses
            yield head
            yield from helper(tail, it)
        else:
            yield from helper(conses, it)

    yield from helper([], it)


import unittest


class TestEachCons(unittest.TestCase):
    def helper(self, each_cons):
        it = range(5)
        out = [list(cons) for cons in each_cons(it, 3)]
        exp = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
        self.assertEqual(exp, out)

    def test_iterative(self):
        self.helper(iterative)

    def test_recursive(self):
        self.helper(recursive)
