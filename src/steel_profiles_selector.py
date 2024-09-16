import structural_analisis
import pandas as pd 


def load_profiles_from_csv(file_path):
    return pd.read_csv(file_path)

def choose_profile(moment, vertical_force , span, profiles_df):
    suitable_profiles = []
    for index, profile in profiles_df.iterrows():
        mcrd_moment = structural_analisis.calculate_Mcrd_moment(profile['plastic_section_modulus'], profile['steel_grade'])
        vcrd_vertical_force = structural_analisis.calculate_Vcrd_vertical_force(profile['section_area'], profile['steel_grade'])

        if mcrd_moment > moment and vcrd_vertical_force > vertical_force:
            print(f'testing Mcrd: {mcrd_moment}, moment: {moment} Vcrd: {vcrd_vertical_force}, V: {vertical_force} ')
            #sprwadzic ugiecia i dopiero dodac do listy
            
            suitable_profiles.append(profile)
    

    return suitable_profiles
