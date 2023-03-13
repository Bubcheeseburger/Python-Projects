# This programs takes in a list of movies that have their name, gross revenue, year, rating, and review numbers. With 
# this information it can then find averages for a category and what movies have a higher rating that a chosen one.

def get_name(movie):
    """
    This function returns the movie title of the movie
    :param movie: This is the movie inputted
    :return: This is the name of the movie
    """
    return movie[0]


def get_gross(movie):
    """
    This function returns the gross earnings of the movie
    :param movie: This is the movie inputted
    :return: This is the gross earning
    """
    return movie[1]


def get_rating(movie):
    """
    This function returns the rating of the movie
    :param movie: This is the movie inputted
    :return: This is the rating
    """
    return movie[3]


def get_num_ratings(movie):
    """
    This function returns the number of ratings of the movie
    :param movie: This is the movie inputted
    :return: This is the number of ratings
    """
    return movie[4]


def better_movies(movie_name, movies_list):
    """
    This functions takes an inputted movie and finds every movie with a higher rating than it
    :param movie_name: This is the inputted movie
    :param movies_list: This is the list of movie that the inputted movie will be compared to
    :return better_movies_list: This returns every movie better than the inputted one
    """
    better_movies_list = []
    for movie in movies_list:  # This for loop goes through every movie and finds one that contains the movie name
        if movie_name in movie:  # If the movie's name is in one of the items listed, this if statement runs
            index = movies_list.index(movie)  # This finds the position of the movie in the list
            rating = get_rating(movies_list[index])  # This finds the rating of the specified movie
    for movie in movies_list:  # This for loop is used to find every movie with a greater rating
        rating2 = get_rating(movie)  # This finds the movies rating
        if rating2 > rating:  # This if statement runs if the movie has a better rating
            better_movies_list.append(movie)  # This adds the movie to the list of movies better than the inputted movie
    return better_movies_list


def average(category, movies_list):
    """
    This function finds the average of either rating, gross, or number of ratings depending on what is inputted
    :param category: This will either be rating, gross, or number of ratings
    :param movies_list: This is the list of movies the average will be taken from
    :return average_num: This is the average of the inputted category
    """
    total = 0  # This is total amount before the number is divided to get the average
    for movie in movies_list:  # This for loop runs through all the movie and totals the number up
        if category == "rating":  # depending on the category inputted, one of these if statements will run
            rating = float(get_rating(movie))
            total += rating
        if category == "gross":
            gross = float(get_gross(movie))
            total += gross
        if category == "number of ratings":
            number = float(get_num_ratings(movie))
            total += number
    average_num = total / len(movies_list)  # The total is divided by the number of movie in order to get the average
    return average_num
