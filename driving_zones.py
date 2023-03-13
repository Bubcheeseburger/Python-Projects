def fine(speed_limit, my_speed, zone="None"):
    """
    This function determines how much the driver will be fined
    :param speed_limit: This is the speed limit displayed
    :param my_speed: This is the driver's speed limit
    :param zone: This is the zone the driver is in
    :return: This is the amount the fine is
    """
    if int(my_speed) < (int(speed_limit) - 10):  # Charge for going too slow
        charge = 30
    elif int(my_speed) >= (int(speed_limit) + 20):  # Charge for reckless driving
        charge = 350
    elif (int(my_speed) >= int(speed_limit)) and zone == "None":  # Normal charge rate in regular speeding zone
        charge = (int(my_speed) - int(speed_limit)) * 6
    elif zone == "residential":  # Charge for speeding in residential zone
        charge = ((int(my_speed) - int(speed_limit)) * 8) + 200
    elif zone == "work" or zone == "school":  # Charge for speeding in school or work zone
        charge = (int(my_speed) - int(speed_limit)) * 7
    else:  # Charge for people going the correct speed
        charge = 0
    return charge


#  charge = (int(my_speed) - int(speed_limit)) * 7
#  charge = ((int(my_speed) - int(speed_limit)) * 8) + 200
def demerits(speed_limit, my_speed):
    """
    What this function seeks to obtain is how many demerit points the driver gets based on their speed
    :param speed_limit: This is the speed limit displayed
    :param my_speed: This is the driver's speed limit
    :return: This is the amount of demerit points
    """
    difference = (int(my_speed) - int(speed_limit))  # This just finds how much over the driver was going
    if 1 <= difference <= 9:  # For 1-9 miles range
        return 3
    elif 10 <= difference <= 19:  # For 10-19 miles range
        return 4
    elif difference >= 20:  # For over 20 miles
        return 6
    else:  # For if the driver is not going over at all
        return 0
