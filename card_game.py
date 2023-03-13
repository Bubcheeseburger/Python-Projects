# This programs simply returns the hard value and soft value of hand according to blackjack standards

def card_to_value(card):
    """
    This function takes the inputted card and gets its value
    :param card: This is the card that has been inputted
    :return value: This is the value of the card inputted
    """
    if card == "A":  # Checks if card is ace, default value is then set to 1
        value = 1
    elif card == "T" or card == "J" or card == "Q" or card == "K":  # Checks for face cards and tens
        value = 10
    else:  # If the values on none of the above, then it is going to be a number value, so the int can now be used
        value = int(card)
    return value


def hard_score(hand):
    """
    This function obtain the value of a hand with aces being the value of 1
    :param hand: This is the list of cards put into the function
    :return hard: This is the value of the hand if all aces are considered 1
    """
    hard = 0  # Setting hard to a default value to be used in the loop
    for card in hand:  # This takes every card in the hand (no matter how many) and adds all their values
        hard += card_to_value(card)  # function is called to get value and sum is cumulated
    return hard


def soft_score(hand):
    """
    This functions simply adds 10 to the hard value to get the soft value if the hand has an ace
    :param hand: This is the hand the user holds
    :return soft: This is the value of the hand if one of the aces (if held) is considered 11
    """
    hard = hard_score(hand)  # Gets the value of hand if it was a hard hand
    if "A" in hand:  # This checks if an ace is in the hand and adds 10 to make on one ace's value 11
        soft = hard + 10
    else:  # If there is no ace, the soft value is the same as the hard value
        soft = hard
    return soft



