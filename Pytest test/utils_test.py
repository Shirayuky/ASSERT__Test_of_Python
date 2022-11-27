import pytest
from utils import double

# pytest видит все что с _test.py or test_
def test_doeble():
    # И здесь уже спокойно пишем assert
    assert double(2) == 4