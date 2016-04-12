
#======================================================================
# Module containing a couple functions to use to allow for commenting
# and blank lines in the material and elemental libray files
#======================================================================

def remove_comments(line):
    import re
    line = re.sub(r'#.*$',"",line)
    return line


def skip_blank_lines(line):
    if line.isspace() == True:
       return True
