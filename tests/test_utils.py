from agentlab.utils import greet, sum_ints


def test_greet():
    assert greet("Tayyab") == "Hello, Tayyab!"


def test_sum_ints():
    assert sum_ints([1, 2, 3]) == 6
