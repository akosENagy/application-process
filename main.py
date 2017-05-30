# APPLICATION-PROCESS SQL QUERY APP
# NOW WITH FLASK :)
####################################################################

# IMPORTS
####################################################################
import psycopg2
import display
import utilities
from flask import Flask

app = Flask(__name__, static_url_path='/static')


# MAIN
####################################################################
def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
