from agentlab.utils import greet, deprecated_sum


def test_greet():
    assert greet("Tayyab") == "Hello, Tayyab!"


def test_deprecated_sum():
    assert deprecated_sum([1, 2, 3]) == 6
