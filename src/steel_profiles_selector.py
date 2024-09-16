import structural_analysis
import load_calculator
import shared_data
import pandas as pd 


def load_profiles_from_csv(file_path):
    return pd.read_csv(file_path)


def choose_profile(span, profiles_df):
    suitable_profiles = []
    for index, profile in profiles_df.iterrows():
    #first calculate loads for self_weight of given profile
        self_weight=structural_analysis.calculate_self_weight(profile['weight(kg/m)'])
        shared_data.dead_load=shared_data.dead_load_base+self_weight
    #calculation of loads:
        total_load = load_calculator.load_sum(
            shared_data.dead_load, shared_data.live_load, 
            shared_data.wind_load, shared_data.snow_load)
        combination_load = load_calculator.load_combination(
            shared_data.dead_load, shared_data.live_load, 
            shared_data.wind_load, shared_data.snow_load)
    #calculation of forces in beam:
        moment = structural_analysis.calculate_moment(total_load, shared_data.span)
        vertical_force = structural_analysis.calculate_vertical_force(combination_load, shared_data.span)
    
    #calculation max forces in given steel section:
        mcrd_moment = structural_analysis.calculate_Mcrd_moment(profile['plastic_section_modulus'], profile['steel_grade'])
        vcrd_vertical_force = structural_analysis.calculate_Vcrd_vertical_force(profile['section_area'], profile['steel_grade'])

        if mcrd_moment > moment and vcrd_vertical_force > vertical_force:
            print(f'testing Mcrd: {mcrd_moment}, moment: {moment} Vcrd: {vcrd_vertical_force}, V: {vertical_force} ')
            #todo: deflection check (span needed)
            #E and I should be taken from steel profile data
            #E = 210GPa, I = 5000cm^4
            ##todo fix constant moment of inertia
            #deflection = structural_analisis.calculate_deflection(total_load, span, 210000, 5000)

            suitable_profiles.append(profile)
    
    return suitable_profiles
