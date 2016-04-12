# Module to parse and read an element library into a single data structure
def grab_chem_symbol(line):
    if line[1] == ' ':
        chem_sym = line[0]
    elif line[1] != ' ':
        chem_sym = line[0,2]
    return chem_sym

def grab_molar_mass(line):
    pass


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


