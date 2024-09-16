#module with simple checks to be updated with load combinations etc.
import load_calculator
import math


def calculate_moment(comb_load, span):
    #max Momentum is equal to (wL^2)/8
    # w - load, L - span
    return (comb_load * span ** 2) / 8

def calculate_vertical_force(comb_load, span):
    return (1/2 * comb_load * span)
    #maksymalna sila przenoszona przez dany przekroj:
    #max value of Vertical force is equal to (A*fy/sqr(3))
    #return (area*(steel_grade/math.sqrt(3)))

def calculate_Mcrd_moment(plastic_section_modulus, steel_grade):
    #plastic section modulus in mm^3, steel grade in kN
    mcrd_moment = plastic_section_modulus * steel_grade /1000
    return mcrd_moment

def calculate_Vcrd_vertical_force(section_area, steel_grade):
    vcrd_vertical_force = section_area*(steel_grade / math.sqrt(3))
    return vcrd_vertical_force

def calculate_deflection(load, span, modulus_of_elasticity, moment_of_inertia):
#     #max deflection is equal to (5wL^4)/384EI
#     # w - load, L - span, E - Youngs module, I - moment of interia
     return (5 * load * span ** 4) / (384 * modulus_of_elasticity * moment_of_inertia)
