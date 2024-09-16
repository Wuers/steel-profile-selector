import load_calculator
import steel_profiles_selector
import structural_analysis

def main():
    #parameters that needs an input:
    # span = float(input("Enter the roof span: "))
    # dead_load = float(input("Enter the dead load: "))
    # live_load = float(input("Enter the live load: "))
    # wind_load = float(input("Enter the wind load: "))
    # snow_load = float(input("Enter the snow load: "))
    span = float(1)
    dead_load = float(2)
    live_load = float(2)
    wind_load = float(1)
    snow_load = float(1)

    total_load = load_calculator.load_sum(dead_load, live_load, wind_load, snow_load)
    combination_load = load_calculator.load_combination(dead_load, live_load, wind_load, snow_load)

    #structural analisys
    #sily w belce:
    moment = structural_analysis.calculate_moment(total_load, span)
    vertical_force = structural_analysis.calculate_vertical_force(combination_load, span)

    #load profiles
    profiles_df = steel_profiles_selector.load_profiles_from_csv(
        "/home/wuer/Documents/Repos/P3_SteelProfilePythonSelector/data/steel_profiles.csv")

    #choosing profiles:
    suitable_profiles = steel_profiles_selector.choose_profile(moment, vertical_force, span, profiles_df)

    #E and I should be taken from steel profile data
    #E = 210GPa, I = 5000cm^4
    ##todo fix constant moment of inertia
    #deflection = structural_analisis.calculate_deflection(total_load, span, 210000, 5000)

    print("All profiles that fits requirments of checking ONLY moment and deflection: ")
    for profile in suitable_profiles:
        print(profile)

if __name__ == "__main__":
    main()