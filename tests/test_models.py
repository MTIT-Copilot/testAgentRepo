from agentlab.models import User


def test_user_display():
    user = User(id=1, name="Alice")
    assert user.display() == "User(1, Alice)"


def test_user_display_different_id():
    user = User(id=42, name="Bob")
    assert user.display() == "User(42, Bob)"


def test_user_display_with_special_characters():
    user = User(id=99, name="O'Neill")
    assert user.display() == "User(99, O'Neill)"
