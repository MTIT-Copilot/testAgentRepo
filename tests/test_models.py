from agentlab.models import User


def test_user_display():
    user = User(id=1, name="Alice")
    assert user.display() == "User(1, Alice)"
