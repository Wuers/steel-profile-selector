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
        self_weight=structural_analysis.calculate_self_weight(profile['Weight'])
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
        mcrd_moment = structural_analysis.calculate_Mcrd_moment(profile['Elastic section modulus'], profile['Steel grade'])
        vcrd_vertical_force = structural_analysis.calculate_Vcrd_vertical_force(
            profile['Area'],profile["Depth"],
            profile["Flange thickness"],profile["Web thickness"],profile["Root radius"], profile['Steel grade'])

        #if mcrd_moment > moment and vcrd_vertical_force > vertical_force:
        if True: 
            deflection = structural_analysis.calculate_deflection(
                total_load, span, shared_data.E, profile["Second moment of area"])
            
            print(f'\n testing: {profile["Profile"]} Mcrd: {mcrd_moment}, moment: {moment} Vcrd: {vcrd_vertical_force}, V: {vertical_force}, deflection: {deflection} ')
            print(f"total_load: {total_load}, combination load: {combination_load}")
            print(f"max def: {shared_data.max_deflection}")
            if deflection < shared_data.max_deflection:
                suitable_profiles.append(profile)
    
    return suitable_profiles