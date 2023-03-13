# This program takes in a dictionary of states with their electoral votes and then declares the winner of the state
# depending of which candidate has the most votes. The winner of the election is outputted when calling "def winner"

results = {}

def add_state(name, votes):
    """
    This function takes in a state name and the votes for that state and then adds the individual with the highest
    votes along with the state into the global dictionary, results
    :param name: This is the name of the state being added and voted for
    :param votes: This is a diction with people and their vote count
    :return: There is no return, but the global variable results is update with the winner and their state
    """
    highest = 0
    winner_person = ""
    global results  # Call global results so that it can be updated by the function
    for candidate in votes.items():  # For loop used to go through every candidate within the dictionary
        if candidate[1] > highest:  # Checks to see if the candidates vote amount is greater than current highest
            highest = candidate[1]  # If it is, updates its votes to be the new highest
            winner_person = candidate[0]  # Winner is also update if they beat the highest
    results[name] = winner_person  # State is key and person is value, state name is unique and auto updates if recalled
    print(results)

def winner(college):
    """
    This function takes in the global dictionary of the states with the individual who won it and gives the winner
    :param college: Has a dictionary of states and their electoral votes
    :return: The candidate with greater than 50% of the votes is returned
    """
    global results
    results_with_numbers = {}  # This list will contain the person as a key and their electoral count as a value
    total = 0
    elected = "No Winner"
    for state in results:  # Goes through every individual diction in the dictionary
        if state not in college:  # If the state won is not an electoral, adds them to dictionary with value of zero
            college[state] = 0
        if state in college:  # Runs if state is in electoral
            if results[state] not in results_with_numbers:  # This creates a dictionary for person if not in new list
                results_with_numbers[results[state]] = college[state]
            elif results[state] in results_with_numbers:  # This adds the electoral vote count on if person on list
                results_with_numbers[results[state]] += college[state]
    for electors in results_with_numbers.values():  # Gets to total amount of electors
        total += electors
    for electors in results_with_numbers.items():  # For every individual, it takes there electoral votes to the total
        percentage = electors[1] / total
        if percentage > 0.5:  # If the individual gets more that 50% votes, he is the new elected.
            elected = electors[0]
    return elected


def clear():
    """
    This function just resets the global list
    :return: Nothing is return, but the global list resets
    """
    results = {}
    global results

