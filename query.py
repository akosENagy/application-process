import utilities


# NEW QUERY FUNCTIONS
####################################################################
# OUTPUT: QUERY RESULTS AS LIST OF TUPLES. TUPLE = ROW             #
####################################################################

def get_mentors():
    '''
    On this page you should show the result of a query that returns the name of the mentors
    plus the name and country of the school (joining with the schools table) ordered by the
    mentors id column (columns: mentors.first_name, mentors.last_name, schools.name, schools.country).
    '''
    results = utilities.run_select_query(
        '''
        SELECT mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
        JOIN schools ON (mentors.city=schools.city) ORDER BY mentors.id;
        ''', ['First Name', 'Last Name', 'School', 'Country']
    )
    return results


def get_all_school():
    '''
    On this page you should show the result of a query that returns the name of the mentors plus
    the name and country of the school (joining with the schools table) ordered by the mentors id column.
    BUT include all the schools, even if there's no mentor yet!
    columns: mentors.first_name, mentors.last_name, schools.name, schools.country
    '''
    results = utilities.run_select_query(
        '''
        SELECT mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
        RIGHT JOIN schools ON (mentors.city=schools.city) ORDER BY mentors.id;
        ''', ['First Name', 'Last Name', 'School', 'Country']
    )
    return results


def get_mentors_by_country():
    '''
    On this page you should show the result of a query that returns the number
    of the mentors per country ordered by the name of the countries
    columns: country, count
    '''
    results = utilities.run_select_query(
        '''
        SELECT schools.country, COUNT(mentors.id) FROM mentors
        JOIN schools ON (mentors.city=schools.city)
        GROUP BY schools.country ORDER BY schools.country ASC;
        ''', ["Country", "Count"]
    )
    return results


def get_contacts():
    '''
    On this page you should show the result of a query that returns the
    name of the school plus the name of contact person at the school
    (from the mentors table) ordered by the name of the school
    columns: schools.name, mentors.first_name, mentors.last_name
    '''
    results = utilities.run_select_query(
        '''
        SELECT schools.name, mentors.first_name, mentors.last_name FROM schools
        JOIN mentors ON (schools.contact_person=mentors.id)
        ORDER BY schools.name ASC;
        ''', ["School", "First Name", "Last Name"]
    )
    return results


def get_applicants():
    '''
    On this page you should show the result of a query that returns the
    first name and the code of the applicants plus the creation_date of the application
    (joining with the applicants_mentors table) ordered by the creation_date in descending order
    BUT only for applications later than 2016-01-01
    columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date
    '''
    results = utilities.run_select_query(
        '''
        SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date FROM applicants
        JOIN applicants_mentors ON (applicants.id=applicants_mentors.applicant_id)
        WHERE (applicants_mentors.creation_date > '2016-01-01')
        ORDER BY applicants_mentors.creation_date DESC;
        ''', ["First Name", "Application Code", "Creation Date"]
    )
    return results


def get_applicants_and_mentors():
    '''
    On this page you should show the result of a query that returns the
    first name and the code of the applicants plus the name of the assigned mentor
    (joining through the applicants_mentors table) ordered by the applicants id column
    Show all the applicants, even if they have no assigned mentor in the database!
    In this case use the string 'None' instead of the mentor name
    columns: applicants.first_name, applicants.application_code, mentor_first_name, mentor_last_name
    '''
    results = utilities.run_select_query(
        '''
        SELECT applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name FROM applicants
        LEFT JOIN applicants_mentors ON (applicants.id=applicants_mentors.applicant_id)
        LEFT JOIN mentors ON (applicants_mentors.mentor_id=mentors.id)
        ORDER BY applicants.id;
        ''', ["A_First Name", "Application Code", "M_First Name", "M_Last Name"]
    )
    return results


####################################################################
# OLD QUERY FUNCTIONS
####################################################################
# INPUT: PSYCOPG2 CONNECTION CURSOR                                #
# OUTPUT: QUERY RESULTS AS LIST OF TUPLES. TUPLE = ROW             #
####################################################################


def get_mentor_names(cursor):
    '''
    Write a query that returns the 2 name columns of the mentors table.
    '''
    columns = ('first_name', 'last_name')
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    result = cursor.fetchall()
    result.insert(0, columns)

    return result


def get_miskolc_nicknames(cursor):
    '''
    Write a query that returns the nick_name-s of all mentors working at Miskolc.
    '''
    column = ('nick_name',)
    cursor.execute("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    result = cursor.fetchall()
    result.insert(0, column)

    return result


def get_carol(cursor):
    '''
    We had interview with an applicant, some Carol. We don't remember her name,
    but she left her hat at the school. We want to call her to give her back her hat.
    To look professional, we also need her full name when she answers the phone (for her full_name,
    you want to include a concatenation into your query, to get her full_name, like: "Carol Something"
    instead of having her name in 2 different columns in the result. This columns should be called: full_name).
    '''
    columns = ('full_name', 'phone_number')
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                   FROM applicants
                   WHERE first_name ='Carol';""")
    result = cursor.fetchall()
    result.insert(0, columns)

    return result


def get_not_carol(cursor):
    '''
    We called Carol, and she said it's not her hat. It belongs to another girl,
    who went to the famous Adipiscingenimmi University.
    You should write a query to get the same informations like with Carol, but for this other girl.
    The only thing we know about her is her school e-mail address ending: '@adipiscingenimmi.edu'.
    '''
    columns = ('full_name', 'phone_number')
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                   FROM applicants
                   WHERE email LIKE '%@adipiscingenimmi.edu';""")
    result = cursor.fetchall()
    result.insert(0, columns)

    return result


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
    columns = ('id', 'first_name', 'last_name', 'phone_numger', 'email', 'application_code')
    cursor.execute("""INSERT INTO applicants
                      (first_name, last_name, phone_number, email, application_code)
                      VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")

    cursor.execute("""SELECT * FROM applicants WHERE application_code=54823;""")
    result = cursor.fetchall()
    result.insert(0, columns)

    return result


def update_jemima(cursor):
    '''
    Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
    Write an UPDATE query, that changes this data in the database for this applicant.
    Also, write a SELECT query, that checks the phone_number column of this applicant.
    Use both of her name parts in the conditions!
    '''
    columns = ("full_name", 'phone_number')
    cursor.execute("""UPDATE applicants
                      SET phone_number='003670/223-7459'
                      WHERE first_name='Jemima' AND last_name='Foreman';""")

    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                      FROM applicants
                      WHERE first_name='Jemima' AND last_name='Foreman';""")
    result = cursor.fetchall()
    result.insert(0, columns)

    return result


def delete_arsenio(cursor):
    '''
    Arsenio, an applicant called us, that he and his friend applied to Codecool.
    They both want to cancel the process, because they got an investor for the site they run: mauriseu.net

    Write DELETE query to remove all the applicants, who applied with emails for this domain
    (e-mail address has this domain after the @ sign).
    '''
    cursor.execute("""DELETE FROM applicants
                      WHERE email LIKE '%@mauriseu.net';""")
    print("\nRows containing @mauriseu.net in email were deleted.")
    return []
