from Scripts.TestItems import TextBoxes
import pytest

@pytest.yield_fixture()
def beforeEachMethod():
    print("Before each and every test case******************")
    yield
    print("After each and every test case******************")
def test_checkTextBox(beforeEachMethod):
    assert 12==12

