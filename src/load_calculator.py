def load_combination(dead_load, live_load, wind_load, snow_load):
    #using simple combination with coefficients of:
    # yG = 1,35 and yQ = 1,5
    combination_load = 1.35 * dead_load + 1.5*(live_load + wind_load + snow_load)    
    return combination_load

def load_sum(dead_load, live_load, snow_load, wind_load):
    return (dead_load+live_load+snow_load+wind_load)