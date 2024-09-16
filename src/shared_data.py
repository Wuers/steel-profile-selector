#values that have to estimated by user (span in [m] rest in [kN/m])
#those are global variables
span = float(5.7) #dead_load_base is dead load without self weight of beam:
dead_load_base = float(9.075)
live_load = float(6.25)
wind_load = float(0)
snow_load = float(0)
max_deflection = (span)*1000/400
#-------------------
#values below this line should not be changed manualy
#dead_load is a true dead load value that is overwritten by app
dead_load = 0
E = 210000
