def gellish2(age):
    # The purpose of this function is the approximate Heart-Rate Max through age
    hrmax = 191.5 - (0.007 * (age ** 2))  # Equation for HR Max
    return hrmax

def in_target_range(hr, age):
    # This function takes in the age of the person and their current HR and sees if it is within the proper range
    low = (191.5 - (0.007 * (age ** 2))) * 0.65  # This equation gets the low threshold of 65%
    high = (191.5 - (0.007 * (age ** 2))) * 0.85  # This equation gets the high threshold of 85%
    statement = low <= hr <= high  # Comparison to see if the HR is within the range
    return statement
