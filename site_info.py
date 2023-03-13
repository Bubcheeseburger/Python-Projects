# Ali Khan (pnv4bs)

import urllib.request


def instructor_lectures(department, instructor):
    """
    This takes in the department of class and the instructor and gives a list of class they teach in that department
    :param department: This is the department of classes (Ex. CS, BIOL, and STS)
    :param instructor: This is the name of the person teaching a class
    :return: This gives back the name of classes a specific teacher is teaching in a specific department
    """
    website_info = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + department)
    class_list = []
    for row in website_info:  # Goes through every row on info on the website
        row = row.decode('utf-8')  # Decodes the info
        cells = row.strip().split('|')  # Creates a list by separating the information
        if instructor in cells[4] and cells[3] not in class_list:
            # If the instructor teaches the class and the class is not in the list, then the class is added to a list
            if "Laboratory" not in cells[3] and "Discussion" not in cells[3]:
                # If the class is a Lab or a Discussion, it will not be added to this list
                class_list.append(cells[3])
    website_info.close()
    return class_list


def compatible_classes(first_class, second_class, needs_open_space=False):
    """
    This functions compares two classes to see if they would be able to fit together in a schedule
    :param first_class: This is one of the class inputted
    :param second_class: This is the other that will be compared to
    :param needs_open_space: If checked, this function will return False if the class is filled up
    :return: True is returned if the class is available and fits, False if not
    """
    available = True
    # This whole section gets all the information of the first class into a list
    first_class_list = first_class.split(" ")
    first_info = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + first_class_list[0])
    first = []
    for row in first_info:
        row = row.decode('utf-8')
        cells = row.strip().split('|')
        if first_class_list[1][0:4] in cells[1] and first_class_list[1][5:8] in cells[2]:
            # If the course number matches and the section does to, then set first to that cell
            first = cells
    first_info.close()

    # This whole section gets all the information of the second class into a list
    second_class_list = second_class.split(" ")
    second_info = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + second_class_list[0])
    second = []
    for row in second_info:
        row = row.decode('utf-8')
        cells = row.strip().split('|')
        if second_class_list[1][0:4] in cells[1] and second_class_list[1][5:8] in cells[2]:
            # If the course number matches and the section does to, then set second to that cell
            second = cells
    second_info.close()

    # This section checks to see if the classes are compatible
    if first[12] <= second[12] <= first[13] or first[12] <= second[13] <= first[13]:
        # If  second start time is the same or inbetween first class time or second end is inbetween second class time
        for number in range(7, 12):
            # For loop goes through all the days from Monday through Friday
            if first[number] == "true" and second[number] == "true":
                # If both of the classes on the same day are true, then they share the same day and time
                available = False
    else:
        available = True
    if needs_open_space:
        # If the class needs to have an open space
        if int(first[15]) >= int(first[16]) or int(second[15]) >= int(second[16]):
            # If the first class is full or the second class is full
            available = False
    return available
