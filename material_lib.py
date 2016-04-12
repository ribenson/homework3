# This is a module containing functions used to parse an input file containing a material library

#======================================================================
# Function used to parse a line into separate values
#======================================================================

def grab_line_info(line):
    line_info_list = line.split()
    return line_info_list


#======================================================================
# Function to Parse first line of each block
#======================================================================

def parse_first_line(line):
    
    line_info_list = grab_line_info(line)
    
    mat_name = line_info_list[0]
    density_stp = line_info_list[1]
    num_of_elem = line_info_list[2]

    return mat_name, density_stp, num_of_elem



#======================================================================
# Function to Parse single element mass fraction line in a block
#======================================================================

def parse_elem_frac(line):

    single_elem_info = grab_line_info(line)

    chem_symbol = single_elem_info[0]
    mass_frac = single_elem_info[1]
    atom_num = single_elem_info[2]

    return chem_symbol, mass_frac, atom_num
    

#======================================================================
# Function to open file and loop over all lines and create material library
#======================================================================

def create_mat_lib(filename, matlib_dict):
    
