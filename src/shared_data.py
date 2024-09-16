#values that have to estimated by user (span in [m] rest in [kN/m])
#those are global variables
span = float(1)
#dead_load_base is dead load without self weight of beam:
dead_load_base = float(2)
live_load = float(2)
wind_load = float(1)
snow_load = float(1)
#-------------------
#dead_load is a true dead load value that is overwritten by app
#and should not be changed manualy
dead_load = 0
