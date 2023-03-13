# This progam takes in a list of a list, where each list has the same number of items. These lists together represent
# a data table. Them means of the whole table can be taken, each row, or each column

def mean_all(table):
    """
    This takes the mean of all the number in the whole table
    :param table: This is the list of list
    :return: This returns the average of every number
    """
    the_ultimate_list = []  # This just takes every number from an individual lists and puts it into a larger list
    total = 0
    for list in table:  # Looks through every list in the list
        for item in list:  # Looks through every item in the list to add it to the larger list
            the_ultimate_list.append(item)
    length = len(the_ultimate_list)  # Length is taking of the new list to obtain average
    for item in the_ultimate_list:  # All the items are then added up
        total += item
    average = total/length  # Average is taken
    return average


def mean_by_row(table):
    """
    This looks through the table and takes the average of the all the numbers within each individual list
    :param table: This is the list of list
    :return: This is the average of the list in the list
    """
    list_of_list = []
    total = 0
    length = 0
    for list in table:  # Looks through the list within in the table
        for item in list: # Looks through the items in the list and adds them up
            total += item
            length = len(list)
        average = total/length  # Obtain the average of the list in the list
        total = 0  # Returns the total back to zero so when it moves onto the next list in the list, it will be default
        list_of_list.append(average)  # Adds the averages to a new list that is then returned
    return list_of_list


def mean_by_col(table):
    """
    This functions takes the average of items within a list columns rather than rows
    :param table: This is the list of list
    :return:
    """
    final_list = []
    count = 0
    columns = len(table[0])
    while count < columns:  # This while loop runs until count is equal to the amount of columns
        total = 0
        amount = 0
        for list in table:  # This goes through every list in the table
            amount += 1  # Amount is how many numbers are in the column
            total += list[0]  # Total is the all the numbers in the column summed up
            list.pop(0)  # Deletes the 1st item in list so that when loop runs again, the next column will be at index 0
        final_list.append((total / amount))  # Adds the average of the column to a new list
        count += 1  # Count goes up in order to close the while loop, closes depending on column amount
    return final_list







