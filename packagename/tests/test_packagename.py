import os
import pytest

from packagename import packagename


def test_hello():
	assert packagename.hello('Sarah') == 'Hello Sarah'
	