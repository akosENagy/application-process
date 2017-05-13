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


# FUNCTIONS
####################################################################
def display_menu():
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
    '''
    Asks for user input (number between 0-7)
    and returns the corresponding function of choice from MENU_OPTIONS
    (Note: Does not call the function.)
    '''
    choice = ''
    while choice not in range(7):
        try:
            choice = int(input('Please enter your choice: ')) - 1

            if choice == -1:
                return 'Exit'
        except ValueError:
            print('Please enter a valid number.')

    return MENU_OPTIONS[choice]


def print_result(result_list):
    '''
    Gets a list of tuples as input, prints them in a table.
    '''
    print()
    if len(result_list) == 0:
        print("No results to display.")
        return None

    max_column_lengths = []
    for i, item in enumerate(result_list[0]):
        lengths_in_column = [len(str(result_list[j][i])) for j in range(len(result_list))]

        max_column_lengths.append(max(lengths_in_column))

        # Print header
        print(str(item) + ' ' * (max_column_lengths[i] - len(item)) + '|', end='')
    print("\n" + "=" * (sum(max_column_lengths) + len(max_column_lengths)))

    # Print the rest of the table
    for row in result_list[1:]:
        for i, item in enumerate(row):
            print(str(item) + ' ' * (max_column_lengths[i] - len(str(item))) + '|', end='')
        print()
