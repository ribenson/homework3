#========================================================================
# This is a module that will take a single material as an input and
# use the element library to generate a list of all the nuclides in that
# material and their isotopic abundances.
#=========================================================================

def list_of_nucs(mat_lib,nuc_dict):
    import element_lib
    material_dict = dict()
    element_dict = dict()
    element_library = element_lib.elem_lib_from_file('elelib.std', element_dict) 
    material_libary = material_lib.create_mat_lib(mat_lib, material_dict)

    for key in material_library:
        empty_dict = dict()
        mat_elem_rho = material_lib[key]['density at STP']

        for subsubkey in mat_dict:
            MM  = element_library[subsubkey]['molar mass']
            wo = material_library['elemental info'][subsubkey]['mass fraction']
            z = material_library['elemental info'][subsubkey]['atomic number']

            for subsubsubkey in element_library[subsubkey]['isotope abundance']:
                ao = element_library[key][subsubkey]['isotope abundace'][subsubsubkey]
                za_id = int(subsubsubkey)+int(z)*1000
                N = float(mat_elem_rho)*float(wo)*float(ao)/float(MM)
                empty_dict[za_id] = N

            nuc_dict[key] = empty_dict


   
