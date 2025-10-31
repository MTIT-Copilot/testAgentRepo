from agentlab.models import User

def test_display_basic():
    user = User(id=1, name="Alice")
    assert user.display() == "User(1, Alice)"
