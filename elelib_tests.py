from nose.tools import assert_equal
from element_lib import parse_first_line as pfl

def test_pfl_1():
    file_name = 'elelib.std'
    obs = pfl(file_name)
    exp = [83, 368]
    assert_equal(obs,exp)


