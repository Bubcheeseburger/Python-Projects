# This program asks the user numerous questions about a player in a basketball game and return a statement that 
# gives that player's statistics

player = input("What player would you like to calculate statistics for? ")
team = input("What team was the opponent in the game you would like to calculate statistics for? ")
three = input("How many 3's did " + player + " attempt this game? ")
three_make = input("How many 3's did " + player + " make this game? ")
two = input("How many 2's did " + player + " attempt this game? ")
two_make = input("How many 2's did " + player + " make this game? ")
free = input("How many free throws did " + player + " attempt this game? ")
free_make = input("How many free throws did " + player + " make this game? ")
field_goal = (int(three_make)+int(two_make)) / (int(three)+int(two))
field_goal *= 100
field_goal = str(field_goal)
free_throw = (int(free_make)/int(free))
free_throw *= 100
free_throw = str(free_throw)
print(player + " had a " + field_goal + "% field goal percentage and a " + free_throw + "% free throw percentage")
points = (int(three_make) * 3) + (int(two_make) * 2) + (int(free_make))
points = str(points)
print(player + " scored " + points + " points against " + team + ". Let's go!")
