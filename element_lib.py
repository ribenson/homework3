# Module to parse and read an element library into a single data structure

#=============================================================
# Group of Functions Used to Parse First Line of Each Block
#=============================================================
def grab_chem_symbol(line):
    if line[1] == ' ':
        chem_sym = line[0]
    elif line[1] != ' ':
        chem_sym = line[0,2]
    return chem_sym

def grab_molar_mass(line):
    molar_mass = line[8:20]
    return molar_mass

def grab_z_number(line):
    element_z = line[22:24]
    element_z = element_z.strip
    return element_z

def grab_density(line):
    density_STP = line[30:42]
    return density_STP

def grab_iso_number(line):
    line_len = len(line.strip())
    iso_number = line[line_len-2:line_len]
    return iso_number

#============================================================
# Function that parses first line of each file and puts it in
# an element library dictionary
#============================================================

def parse_first_line(file_name):
    import re
    input_file = open(file_name)
    element_cnt = 0
    line_count = 0

    for line in input_file:
        if re.match("[a-z]",line[0]):
            element_cnt = element_cnt + 1
        line_count = line_count + 1
    
    return [element_cnt, line_count]


