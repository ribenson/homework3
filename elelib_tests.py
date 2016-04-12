from nose.tools import assert_equal
from element_lib import parse_first_line as pfl
from element_lib import grab_chem_symbol, grab_molar_mass, grab_z_number
from element_lib import grab_density, grab_iso_number
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

def test_molar_mass():
    input_file = open('element_sample.std')
    for line in input_file:
        obs = grab_molar_mass(line)
        return obs
    exp = '0.100790E+01'
    assert_equal(obs,exp)

def test_z_number():
    input_file = open('element_sample.std')
    for line in input_file:
        obs = grab_z_number(line)
        return obs
    exp = '1'

def test_density():
    input_file = open('element_sample.std')
    for line in input_file:
        obs = grab_density(line)
        return obs
    exp = '0.899000E-04'

def test_iso_number():
    input_file = open('element_sample.std')
    for line in input_file:
        obs = grab_iso_number(line)
        return obs
    exp = '2'
