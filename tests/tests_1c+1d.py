import pytest
from labs.lab_1.lab_1c import max_subarray_sum
from labs.lab_1.lab_1d import two_sum

def test_max_subarray_sum_standard():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_all_negative():
    # This specifically tests the bug where max_global was incorrectly handled
    assert max_subarray_sum([-5, -1, -3]) == -1

def test_two_sum_standard():
    # This checks the bug where 'complement' was adding instead of subtracting
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 20) == []