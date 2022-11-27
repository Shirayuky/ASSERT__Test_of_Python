import pytest
from divide import divide


class TestPositiveInt:
    def test_positive(self):
        assert divide(100, 10) == 10.0

    def test_negative(self):
        assert divide(-20, -5) == 4.0

    def test_zero(self):
        assert divide(0, 2) == 0.0

    def test_float(self):
        assert divide(2.2, 2) == 1.1

    def test_type_mismatch(self):
        '''Преждевременно узнавая ошибку'''
        with pytest.raises(TypeError):
            divide(True, None)

    def test_zero_division(self):
        '''Преждевременно узнавая ошибку'''
        with pytest.raises(ZeroDivisionError):
            divide(100, 0)
