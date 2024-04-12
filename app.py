from wtforms import Form, StringField, SubmitField, validators
from flask import Flask, render_template, request
from classes import Temperature, CalcCalories
from flask.views import MethodView
from talisman import Talisman
from bleach import clean

# Configure application
app = Flask(__name__)
# security enforce to use HTTPS and more
Talisman(app)


class CaloriesForm(Form):
    """ class for retrieving data from user"""
    # making fields in python instead of HTML, using validators from flask
    weight = StringField('Weight: ', [validators.DataRequired()])
    height = StringField('Height: ', [validators.DataRequired()])
    age = StringField('Age: ', [validators.DataRequired()])

    city = StringField('City: ', [validators.DataRequired()])
    country = StringField('County: ', [validators.DataRequired()])
    # adding button for submit info
    button = SubmitField('Calculate', [validators.DataRequired()])


class HomePage(MethodView):
    """ class for rendering Home page """
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):
    """ render page for submitting info """
    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html',
                               caloriesform=calories_form)


    def post(self):
        caloriesform = CaloriesForm(request.form)

        # Sanitize user input using Bleach
        weight = clean(caloriesform.weight.data)
        height = clean(caloriesform.height.data)
        age = clean(caloriesform.age.data)

        try:
            weight = float(caloriesform.weight.data)
            height = float(caloriesform.height.data)
            age = float(caloriesform.age.data)
        except ValueError:
            print('Input must be float number')
        # backend scraping data for given country/city
        try:
            # also clean input of user to prevent XSS attacks
            city = clean(caloriesform.city.data)
            country = clean(caloriesform.country.data)
        except ValueError:
            print('City or country not found')

        temperature = Temperature(country=country, city=city).scrape_temp()
        # calculate BMR
        bmr = CalcCalories(weight=weight, height=height,
                           age=age, temperature=temperature).calculate()
        return render_template('calories_form_page.html', caloriesform=caloriesform, bmr=bmr)


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))


app.run(debug=True)
