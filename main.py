# APPLICATION-PROCESS SQL QUERY APP
# NOW WITH FLASK :)
####################################################################

# IMPORTS
####################################################################
import query
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')


# ROUTE FUNCTIONS
####################################################################

@app.route('/')
def render_main_page():
    return render_template('index.html')


@app.route('/mentors')
def get_mentors():
    mentors = query.get_mentors()
    return render_template('result.html', results=mentors)


@app.route('/all-school')
def get_all_school():
    results = query.get_all_school()
    return render_template('result.html', results=results)


@app.route('/mentors-by-country')
def get_mentors_by_country():
    results = query.get_mentors_by_country()
    return render_template('result.html', results=results)


@app.route('/contacts')
def get_contacts():
    contacts = query.get_contacts()
    return render_template('result.html', results=contacts)


@app.route('/applicants')
def get_applicants():
    applicants = query.get_applicants()
    return render_template('result.html', results=applicants)


@app.route('/applicants-and-mentors')
def get_applicants_and_mentors():
    applicants_and_mentors = query.get_applicants_and_mentors()
    return render_template('result.html', results=applicants_and_mentors)


# MAIN
####################################################################
def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
