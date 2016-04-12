from nose.tools import assert_equal
from element_lib import parse_first_line as pfl
from element_lib import grab_chem_symbol, grab_molar_mass, grab_z_number
from element_lib import grab_density, grab_num_of_iso
from element_lib import parse_isotopic_abund as pia
from element_lib import elem_lib_from_file as elff
from utility_funcs import remove_comments, skip_blank_lines
import re


def test_pfl_1():
    input_file = open('element_sample.std')
    for line in input_file:
        if re.match("[a-z]",line[0]):
            obs = pfl(line)
    exp = ['h', '0.100790E+01', '1', '0.899000E-04', '2']
    assert_equal(obs,exp)

def test_chem_sym():
    input_file = open('element_sample.std')
    for line in input_file:
        if re.match("[a-z]",line[0]):
            obs = grab_chem_symbol(line)
    exp = 'h'
    assert_equal(obs,exp)

def test_molar_mass():
    input_file = open('element_sample.std')
    for line in input_file:
        if re.match("[a-z]",line[0]):
            obs = grab_molar_mass(line)
    exp = '0.100790E+01'
    assert_equal(obs,exp)

def test_z_number():
    input_file = open('element_sample.std')
    for line in input_file:
        if re.match("[a-z]",line[0]):
            obs = grab_z_number(line)
    exp = '1'
    assert_equal(obs,exp)

def test_density():
    input_file = open('element_sample.std')
    for line in input_file:
        if re.match("[a-z]",line[0]):
            obs = grab_density(line)
    exp = '0.899000E-04'
    assert_equal(obs,exp)

def test_num_of_iso():
    input_file = open('element_sample.std')
    for line in input_file:
        if re.match("[a-z]",line[0]):
            obs = grab_num_of_iso(line)
    exp = '2'
    assert_equal(obs,exp)

def test_pia_1():
    input_file = open('element_sample.std')
    for line in input_file:
        if line[0] == ' ':
            obs = pia(line)
    exp = ['2', '0.150000E-01']
    assert_equal(obs,exp)

def test_elem_lib():
    input_file = open('element_sample.std')
    input_dict = {}
    obs = elff(input_file,input_dict)
    exp = {'h':{'Z':'1', 'density':'0.899000E-04', 'molar mass': '0.100790E+01', 'number of natural isotopes': '2','isotope abundance':{1001:'0.999850E+02',1002:'0.150000E-01'}}}
    assert_equal(obs,exp)

def test_elem_lib_2():
    input_file = open('elelib.std')
    input_dict = {}
    elem_lib = elff(input_file,input_dict)
    obs = elem_lib['he']
    exp = {'Z': '2', 'density': '0.178700E-03', 'molar mass': '0.400260E+01', 'number of natural isotopes': '2','isotope abundance': {2003: '0.100000E-03', 2004: '0.100000E+03'}}
    assert_equal.__self__.maxDiff = None
    assert_equal(obs,exp)

def test_elem_lib_3():
    input_file = open('elelib.std')
    input_dict = {}
    elem_lib = elff(input_file,input_dict)
    obs = elem_lib['o']['isotope abundance'][8016]
    exp = '0.997590E+02'
    assert_equal(obs,exp)

def test_elem_lib_4():
    input_file = open('elelib_comment.std')
    input_dict = {}
    obs1 = elff(input_file,input_dict)
    obs = obs1['h']
    exp = {'Z':'1', 'density':'0.899000E-04', 'molar mass': '0.100790E+01', 'number of natural isotopes': '2','isotope abundance':{1001:'0.999850E+02',1002:'0.150000E-01'}}
    assert_equal(obs,exp)

def test_elem_lib_5():
    input_file = open('elelib_comment.std')
    input_dict = {}
    elem_lib = elff(input_file,input_dict)
    obs = elem_lib['he']
    exp = {'Z': '2', 'density': '0.178700E-03', 'molar mass': '0.400260E+01', 'number of natural isotopes': '2','isotope abundance': {2003: '0.100000E-03', 2004: '0.100000E+03'}}
    assert_equal.__self__.maxDiff = None
    assert_equal(obs,exp)

def test_elem_lib_6():
    input_file = open('elelib_comment.std')
    input_dict = {}
    elem_lib = elff(input_file,input_dict)
    obs = elem_lib['o']['isotope abundance'][8016]
    exp = '0.997590E+02'
    assert_equal(obs,exp)
