def init_db_connection(connection_string):
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
