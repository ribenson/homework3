from nose.tools import assert_equal
from element_lib import parse_first_line as pfl
from element_lib import grab_chem_symbol

def test_pfl_1():
    file_name = 'elelib.std'
    obs = pfl(file_name)
    exp = [83, 368]
    assert_equal(obs[0:2],exp)

def test_chem_sym():
    input_file = open('element_sample.std')
    for line in input_file:
        obs = grab_chem_symbol(line)
        return obs
    exp = 'h'
    assert_equal(obs,exp)
