import load_calculator
import steel_profiles_selector
import structural_analysis
import shared_data

def main():
    #load profiles
    profiles_df = steel_profiles_selector.load_profiles_from_csv(
        #linux path
        #"/home/wuer/Documents/Repos/P3_SteelProfilePythonSelector/data/steel_profiles.csv"
        #windows path:
        "F:\0_Wuer\5 Projekty\Python\P4_SteelProfileSelector\data\steel_profiles.csv"
        )

    #choosing profiles:
    suitable_profiles = steel_profiles_selector.choose_profile(shared_data.span, profiles_df)

    print("All profiles that fits requirments of checking ONLY moment and deflection: ")
    for profile in suitable_profiles:
        print(profile)

if __name__ == "__main__":
    main()