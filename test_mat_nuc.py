from mat_nuc_list import list_of_nucs
from nose.tools import assert_equal
from material_lib import grab_line_info, parse_first_line, parse_elem_frac, create_mat_lib
from utility_funcs import remove_comments, skip_blank_lines
from element_lib import parse_first_line as pfl
from element_lib import grab_chem_symbol, grab_molar_mass, grab_z_number
from element_lib import grab_density, grab_num_of_iso
from element_lib import parse_isotopic_abund as pia
from element_lib import elem_lib_from_file as elff


def test_list_nucs():
    file_name = 'matlib.sample'
    dict_start = dict()
    material_lib = create_mat_lib(file_name,dict_start)
    nuc_dict = dict()
    
    nuc_list = list_of_nucs(material_lib,nuc_dict)
    obs = nuc_list['BRONZE']['elemental info']['cu']['atomic number']
    exp = '29'
