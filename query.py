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


def get_not_carol(cursor):
    '''
    We called Carol, and she said it's not her hat. It belongs to another girl,
    who went to the famous Adipiscingenimmi University.
    You should write a query to get the same informations like with Carol, but for this other girl.
    The only thing we know about her is her school e-mail address ending: '@adipiscingenimmi.edu'.
    columns: full_name, phone_number
    '''
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                   FROM applicants
                   WHERE email LIKE '%@adipiscingenimmi.edu';""")
    return cursor.fetchall()


def insert_marcus(cursor):
    '''
    After we returned the hat, a new applicant appeared at the school,
    and he wants to get into the application process.
    His name is Markus Schaffarzyk, has a number: 003620/725-2666
    and e-mail address: djnovus@groovecoverage.com
    Our generator gave him the following application code: 54823

    After INSERTing the data, write a SELECT query, that returns with
    all the columns of this applicant! (use the unique application code for your condition!)
    '''
    cursor.execute("""INSERT INTO applicants
                      (first_name, last_name, phone_number, email, application_code)
                      VALUES ('Markus', 'Schaffarzyk', 003620/725-2666, 'djnovus@groovecoverage.com', 54823);""")

    cursor.execute("""SELECT * FROM applicants WHERE application_code=54823;""")
    return cursor.fetchall()