# IMPORTS
####################################################################
import query


# CONSTANTS
####################################################################
MENU_OPTIONS = {
    0: query.get_mentor_names,
    1: query.get_miskolc_nicknames,
    2: query.get_carol,
    3: query.get_not_carol,
    4: query.insert_marcus,
    5: query.update_jemima,
    6: query.delete_arsenio
}


def display_menu():
    '''
    Displays menu and returns the function of choice from MENU_OPTIONS
    (Note: Does not call the function.)
    '''
    print('\nPlease choose one of the following options:\n')
    print('(0) - Exit application')
    print('(1) - Names of the mentors')
    print('(2) - Nicknames of Miskolc mentors')
    print('(3) - Find Carol\'s phone number')
    print('(4) - Find @adipiscingenimmi.edu emails')
    print('(5) - Insert Markus Schaffarzyk')
    print('(6) - Update Jemima Foreman\'s email')
    print('(7) - Delete @mauriseu.net emails')


def get_choice():
    choice = ''
    while choice not in range(7):
        try:
            choice = int(input('Please enter your choice: ')) - 1

            if choice == -1:
                return 'Exit'
        except ValueError:
            print('Please enter a valid number.')

    return MENU_OPTIONS[choice]


