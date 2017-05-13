# APPLICATION-PROCESS SQL QUERY APP
####################################################################

# IMPORTS
####################################################################
import psycopg2


# QUERY FUNCTIONS
####################################################################
# INPUT: PSYCOPG2 CONNECTION CURSOR                                #
# OUTPUT: QUERY RESULTS AS LIST OF TUPLES. TUPLE = ROW             #
####################################################################
def get_mentor_names(cursor):
    '''
    Write a query that returns the 2 name columns of the mentors table.
    columns: first_name, last_name
    '''
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    return cursor.fetchall()


def get_miskolc_nicknames(cursor):
    '''
    Write a query that returns the nick_name-s of all mentors working at Miskolc.
    column: nick_name
    '''
    cursor.execute("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    return cursor.fetchall()


def get_carol(cursor):
    '''
    We had interview with an applicant, some Carol. We don't remember her name,
    but she left her hat at the school. We want to call her to give her back her hat.
    To look professional, we also need her full name when she answers the phone (for her full_name,
    you want to include a concatenation into your query, to get her full_name, like: "Carol Something"
    instead of having her name in 2 different columns in the result. This columns should be called: full_name).
    columns: full_name, phone_number
    '''
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                   FROM applicants
                   WHERE first_name ='Carol';""")
    return cursor.fetchall()


# MAIN
####################################################################
def main():
    try:
        # setup connection string
        connect_str = "dbname='aakeeka' user='aakeeka' host='localhost' password='postgresql'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()

    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

if __name__ == '__main__':
    main()
