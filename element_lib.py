# Module to parse and read an element library into a single data structure

#======================================================================
# Function used to parse a line into separate values
#======================================================================

def grab_line_info(line):
    line_info_list = line.split()
    return line_info_list

#=============================================================
# Group of Functions Used to Parse First Line of Each Block
#=============================================================
def grab_chem_symbol(line):
    line_info = grab_line_info(line)
    chem_sym = line_info[0]
    return chem_sym

def grab_molar_mass(line):
    line_info = grab_line_info(line)
    molar_mass = line_info[1]
    return molar_mass

def grab_z_number(line):
    line_info = grab_line_info(line)
    element_z = line_info[2]
    return element_z

def grab_density(line):
    line_info = grab_line_info(line)
    density_STP = line_info[3]
    return density_STP

def grab_num_of_iso(line):
    line_info = grab_line_info(line)
    num_of_iso = line_info[4]
    return num_of_iso

#===================================================================
# Function that parses the first line of a block
#===================================================================

def parse_first_line(line):
    chem_sym = grab_chem_symbol(line)
    molar_mass = grab_molar_mass(line)
    element_z = grab_z_number(line)
    density_STP = grab_density(line)
    num_of_iso = grab_num_of_iso(line)
    
    return [chem_sym, molar_mass, element_z, density_STP, num_of_iso]


#===================================================================
# Function that parses the isotopic abundance information from rest
# of the block.
#===================================================================

def parse_isotopic_abund(line):
    line_info = grab_line_info(line)
    iso_mass_num = line_info[0]
    iso_abund = line_info[1]

    return [iso_mass_num, iso_abund]



#======================================================================
# Function to open the file and loop over all the lines creating 
# the element library by calling the above functions.
#======================================================================

def elem_lib_from_file(filename, input_dict):
    import re
    from utility_funcs import remove_comments, skip_blank_lines
    
    for line in filename:
        line = remove_comments(line)

        if skip_blank_lines(line) == True:
            continue

        elif re.match("[a-z]",line[0]):
            isotope_data = {}
            element_info = parse_first_line(line)

            chem_sym = element_info[0]
            molar_mass = element_info[1]
            element_z = element_info[2]
            density_STP = element_info[3]
            num_of_iso = element_info[4]

        elif line[0] == ' ':
            abund_info = parse_isotopic_abund(line)
            ZZZAAA_id = int(element_z)*1000+int(abund_info[0])

            isotope_data[ZZZAAA_id] = abund_info[1]

        input_dict[chem_sym] = {'molar mass':molar_mass, 'Z':element_z, 'density':density_STP, 'number of natural isotopes':num_of_iso, 'isotope abundance':isotope_data}

    return input_dict

