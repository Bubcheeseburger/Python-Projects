first_number = input("Pick a number between 1 and 10: ")
new_number = ((int(first_number) * 2) + 5) * 50
birthday = input("If you've already had a birthday this year, enter 1772. Otherwise, enter 1771: ")
birthday = int(birthday)
new_number = new_number + birthday
birth_year = input("Enter the year that you were born: ")
magic_number = new_number - (int(birth_year))
age = magic_number - (int(first_number) * 100)
print('The magic number is "' + str(magic_number) + '". That means you are ' + str(age) + '!')
