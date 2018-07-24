def each_slice(it, size):
  current_slice = []
  for i in it:
    current_slice.append(i)
    if len(current_slice) == size:
      yield current_slice
      current_slice = []
  if current_slice:
    yield current_slice


import unittest
import itertools

class TestEachSlice(unittest.TestCase):
  def test_each_slice(self):
        i = range(5);
        o = [list(slice) for slice in each_slice(i, 2)]
        e = [[0, 1], [2, 3], [4]]
        self.assertEqual(o, e)
