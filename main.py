# APPLICATION-PROCESS SQL QUERY APP
# NOW WITH FLASK :)
####################################################################

# IMPORTS
####################################################################
import psycopg2
import display
import utilities
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


# ROUTE FUNCTIONS
####################################################################

@app.route('/')
def render_main_page():
    return render_template('index.html')


# MAIN
####################################################################
def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
