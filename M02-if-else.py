 # Daniel Bautista
# M02 Case Study: if...else and while
# the app will show if the student qualifies for the Dean's List, Honor Roll, or neither

gpa1 = 3.5
gpa2 = 3.25
QUIT = 'ZZZ'

while True:
    lastname = input('Please enter your last name (or enter "ZZZ" to quit): ')  # has the user input their last name

    if lastname == 'ZZZ':
        break  # exit the loop if the user enters "ZZZ"

    firstname = input('Please enter your first name: ')  # has the user input their first name
    gpa = float(input('Please enter your GPA: '))  # has the user input their GPA

    if gpa >= gpa1:
        print(firstname + '', lastname + ' has made the Dean\'s List.')
    elif gpa1 >= gpa >= gpa2:
        print(firstname + '', lastname + ' has made the Honor Roll.')
    else:
        print(firstname + '', lastname + ' has made neither list.')
