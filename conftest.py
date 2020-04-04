import pytest
from pyexpect import expect

from pybraries.subscribe import Subscribe


def to_be_a_list_of(self, subtype):
    expect(type(self._actual)).to_be(list)
    for item in self._actual:
        self._assert(type(item) == subtype, f"to be a list of {subtype.__name__}")


expect.to_be_a_list_of = expect.list_of = to_be_a_list_of


def has_substring(self, substring, *other_substrings):
    all_substrings = [substring, *other_substrings]
    self._assert(
        any([self._actual.find(s) != -1 for s in all_substrings]),
        f"to have any of {all_substrings} as substring",
    )


expect.has_substring = (
    expect.to_have_substring
) = expect.to_have_any_of_substrings = has_substring


def of_size(self, size):
    self._assert(
        len(self._actual) == size,
        f"to have a size equal to {size}, but it's {len(self._actual)}",
    )


expect.of_size = expect.to_have_size = of_size


def has_same_size_as(self, target):
    self.of_size(len(target))


expect.has_same_size_as = expect.to_have_same_size_as = has_same_size_as


# unsubscribe from pandas
@pytest.fixture
def pre_sub():
    a = Subscribe()
    a.subscribe("pypi", "pandas")


# subscribe to pandas
@pytest.fixture
def pre_unsub():
    b = Subscribe()
    b.unsubscribe("pypi", "pandas")
