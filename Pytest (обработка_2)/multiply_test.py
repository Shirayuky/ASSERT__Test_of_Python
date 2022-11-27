import pytest
from multiply import multiply


class TestMultiply:
    def test_a(self):
        with pytest.raises(ValueError):
            multiply(10.0, 0)

    def test_b(self):
        with pytest.raises(ValueError):
            multiply(0, 10.0)

    def test_both(self):
        with pytest.raises(ValueError):
           multiply(10.0, 5.0)
