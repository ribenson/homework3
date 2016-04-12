from nose.tools import assert_equal
from material_lib import grab_line_info, parse_first_line, parse_elem_frac
from material_lib import create_mat_lib
from utility_funcs import remove_comments, skip_blank_lines

def test_line_parsing():
    file_name = open('matlib_testing.sample')
    for line in file_name:
        if line[0] != ' ':
            obs = grab_line_info(line)
    exp = ['WALLOY', '0.18130e+02', '5']
    assert_equal(obs,exp)

def test_line_parsing_2():
    file_name = open('matlib_testing.sample')
    for line in file_name:
        if line[0] == ' ':
            outp = grab_line_info(line)
            obs = outp[0]
        exp = 'w'
    assert_equal(obs,exp)

def test_first_line():
    file_name = open('matlib_testing.sample')
    for line in file_name:
        if line[0] != ' ':
            output = parse_first_line(line)
            obs = output[2]
        exp = '5'
    assert_equal(obs,exp)

def test_p_elem_frac():
    file_name = open('matlib_testing.sample')
    for line in file_name:
        if line[0] == ' ':
            output = parse_elem_frac(line)
            obs = output[2]
            exp = '74'
    assert_equal(obs,exp)

def test_create_mat_lib():
    file_name = 'matlib_testing.sample'
    WALLOY_dict = {}

    output = create_mat_lib(file_name, WALLOY_dict)
    obs = output['WALLOY']['elemental info']['fe']['mass fraction']
    exp = '0.73000e+00'
    assert_equal(obs,exp)

def test_create_mat_lib_2():
    file_name = 'matlib_comment.sample'
    WALLOY_dict = {}

    output = create_mat_lib(file_name, WALLOY_dict)
    obs = output['WALLOY']['elemental info']['fe']['mass fraction']
    exp = '0.73000e+00'
    assert_equal(obs,exp)
