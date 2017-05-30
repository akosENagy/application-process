from utilities import run_select_query


# QUERY FUNCTIONS
####################################################################
# OUTPUT: QUERY RESULTS AS LIST OF TUPLES. TUPLE = ROW             #
####################################################################

def get_mentors():
    '''
    On this page you should show the result of a query that returns the name of the mentors
    plus the name and country of the school (joining with the schools table) ordered by the
    mentors id column (columns: mentors.first_name, mentors.last_name, schools.name, schools.country).
    '''
    results = run_select_query(
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
    results = run_select_query(
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
    results = run_select_query(
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
    results = run_select_query(
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
    results = run_select_query(
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
    results = run_select_query(
        '''
        SELECT applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name FROM applicants
        LEFT JOIN applicants_mentors ON (applicants.id=applicants_mentors.applicant_id)
        LEFT JOIN mentors ON (applicants_mentors.mentor_id=mentors.id)
        ORDER BY applicants.id;
        ''', ["A_First Name", "Application Code", "M_First Name", "M_Last Name"]
    )
    return results
