import pytest

from Scripts.TestItems import TextBoxes, tables, Links
driver = None
@pytest.yield_fixture()
def beforeEachMethod():
    print("==============================================================================================================Before each and every test case******************")
    yield
    driver.close()
    print("==============================================================================================================After each and every test case******************")



def test_textBoxesTest(beforeEachMethod):
    global driver
    TextBoxes.verify_textBoxes()
    driver = TextBoxes.driver

def test_tables(beforeEachMethod):
    global driver
    tables.tablestest()
    driver = tables.driver

def test_links(beforeEachMethod):
    global driver
    Links.linksTest()
    driver = Links.driver



# @pytest.fixture()
# def setumodule():
#     print("************ set up **************")
#     return
#
# def tearmodule(module):
#     print("************ tear down **************")
#
#
# @pytest.mark.skipif(False,reason="skipping to test skip")
# def test_first(setumodule):
#     assert 0==0
# @pytest.mark.skipif(False,reason="conditional skip")
# def test_first_two(setumodule):
#     assert 0==0
#
# def test_first_three(setumodule):
#     assert 0==0
#
# @pytest.mark.parametrize('n1,n2',
#                          [
#                              (2,3),('a','b'),(1,'h')
#                           ])
# def test_param(n1,n2):
#     print("\n" + str(n1) + "--" + str(n2))