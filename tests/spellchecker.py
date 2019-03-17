import pytest
from spellchecker import Spellchecker


@pytest.fixture
def spellchecker_setup():
    return Spellchecker()


def test_spellchecker_correction(spellchecker_setup):
    assert spellchecker_setup.check('tests')


def test_spellchecker_correction_list(spellchecker_setup):
    assert len(spellchecker_setup.check_list(['one', 'two', 'three'])) == 0


def test_spellchecker_incorrect(spellchecker_setup):
    assert spellchecker_setup.check('test1') is False


def test_spellchecker_suggestions(spellchecker_setup):
    suggest = spellchecker_setup.suggest('test1')
    assert suggest[0] == 'test'
