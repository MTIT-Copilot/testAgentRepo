from agentlab.models import User

def test_display_basic():
    user = User(id=1, name="Alice")
    assert user.display() == "User(1, Alice)"

def test_display_different_user():
    user = User(id=42, name="Bob")
    assert user.display() == "User(42, Bob)"

def test_display_with_special_chars():
    user = User(id=3, name="O'Brien")
    assert user.display() == "User(3, O'Brien)"
