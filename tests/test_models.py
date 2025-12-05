from agentlab.models import User


def test_display_basic():
    user = User(id=1, name="Alice")
    assert user.display() == "User(1, Alice)"


def test_display_different_id():
    user = User(id=42, name="Bob")
    assert user.display() == "User(42, Bob)"


def test_display_zero_id():
    user = User(id=0, name="Charlie")
    assert user.display() == "User(0, Charlie)"


def test_display_negative_id():
    user = User(id=-1, name="Dave")
    assert user.display() == "User(-1, Dave)"


def test_display_long_name():
    user = User(id=1, name="VeryLongNameWithManyCharacters")
    assert user.display() == "User(1, VeryLongNameWithManyCharacters)"


def test_display_name_with_spaces():
    user = User(id=5, name="John Doe")
    assert user.display() == "User(5, John Doe)"


def test_display_empty_name():
    user = User(id=10, name="")
    assert user.display() == "User(10, )"


def test_display_special_characters():
    user = User(id=7, name="O'Brien")
    assert user.display() == "User(7, O'Brien)"
