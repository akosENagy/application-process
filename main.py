import psycopg2


def get_mentor_names(cursor):
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    return cursor.fetchall()


def get_miskolc_nicknames(cursor):
    cursor.execute("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    return cursor.fetchall()


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
