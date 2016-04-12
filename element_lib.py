# Module to parse and read an element library into a single data structure

#=============================================================
# Group of Functions Used to Parse First Line of Each Block
#=============================================================
def grab_chem_symbol(line):
    chem_sym = line[0:2]
    chem_sym = chem_sym.strip()
    return chem_sym

def grab_molar_mass(line):
    molar_mass = line[8:20]
    return molar_mass

def grab_z_number(line):
    element_z = line[22:24]
    element_z = element_z.strip()
    return element_z

def grab_density(line):
    density_STP = line[30:42]
    return density_STP

def grab_num_of_iso(line):
    line_len = len(line.strip())
    num_of_iso = line[line_len-1:line_len]
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
    line = line.strip()
    iso_mass_num = line[0:3]
    iso_mass_num = iso_mass_num.strip()

    iso_abund = line[-12:]

    return [iso_mass_num, iso_abund]



#======================================================================
# Function to open the file and loop over all the lines creating 
# the element library by calling the above functions.
#======================================================================

def elem_lib_from_file(filename, input_dict):
    import re

    for line in filename:
        if re.match("[a-z]",line[0]):
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

