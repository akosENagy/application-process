# APPLICATION-PROCESS SQL QUERY APP
####################################################################

# IMPORTS
####################################################################
import psycopg2
import query
import display


# MAIN
####################################################################
def main():
    query_to_run = ''
    while query_to_run != 'Exit':
        try:
            # setup connection string
            connect_str = "dbname='aakeeka' user='aakeeka' host='localhost' password='postgresql'"
            # use our connection values to establish a connection
            conn = psycopg2.connect(connect_str)
            # set autocommit option, to do every query when we call it
            conn.autocommit = True
            # create a psycopg2 cursor that can execute queries
            cursor = conn.cursor()

            display.display_menu()
            query_to_run = display.get_choice()

            if callable(query_to_run):
                display.print_result(query_to_run(cursor))
                input('\nPress enter to return to menu...')

        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)

if __name__ == '__main__':
    main()
