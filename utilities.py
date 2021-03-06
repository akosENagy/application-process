import psycopg2

CONNECTION_STRING = "dbname='approc' user='aakeeka' host='localhost' password='postgresql'"


def init_db_connection(connection_string=CONNECTION_STRING):
    '''
    Returns a psycopg2 cursor after connecting with the specified string.
    Connection string format: "dbname='dbname' user='user' host='host' password='password'"
    '''
    conn = psycopg2.connect(connection_string)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    return cursor


def run_select_query(query_string, header):
    '''
    Receives a query string for a select statement, appends a header and returns results as a list of tuples.
    '''
    cursor = init_db_connection()
    cursor.execute(query_string)
    results = cursor.fetchall()
    results.insert(0, header)

    return results
