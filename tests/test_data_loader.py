import pytest
from agentlab.data_loader import process_data, normalize


def test_normalize_basic():
    assert normalize(-5) == 0
    assert normalize(2) == 2


def test_process_data():
    assert process_data([1, -1, 2]) == 3


def test_process_data_none_raises():
    # Demonstrates a gap: current implementation will raise TypeError naturally.
    # This test expects an explicit ValueError to steer the agent to add validation.
    with pytest.raises(ValueError):
        process_data(None)  # type: ignore[arg-type]
