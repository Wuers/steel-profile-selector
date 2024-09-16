#module with simple checks to be updated with load combinations etc.
import load_calculator
import math

#function for selector.choose_profile to calculate self_weith and loads:
def calculate_self_weight(mass_per_m):
    return (mass_per_m*9.81/1000)

def calculate_moment(comb_load, span):
    #max Momentum is equal to (wL^2)/8
    # w - load, L - span
    return (comb_load * span ** 2) / 8

def calculate_vertical_force(comb_load, span):
    return (1/2 * comb_load * span)

def calculate_Mcrd_moment(plastic_section_modulus, steel_grade):
    #plastic section modulus in mm^3, steel grade in kN
    mcrd_moment = plastic_section_modulus * steel_grade /1000
    return mcrd_moment

def calculate_Vcrd_vertical_force(section_area,b,tf,tw,r,steel_grade):
    active_area=section_area*100-2*b*tf+(tw+2*r)*tf
    vcrd_vertical_force = active_area*(steel_grade/math.sqrt(3)/1000)
    return vcrd_vertical_force

def calculate_deflection(load, span, young_module, moment_of_inertia):
#     #max deflection is equal to (5wL^4)/384EI
#     # w - load, L - span, E - Youngs module, I - moment of interia
     return ((5 * load * span ** 4) / (384 * young_module * moment_of_inertia))*1000000
