from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie_webapp import calorie
from calorie_webapp import temperature


app = Flask(__name__)

class LandingPage(MethodView):

    def get(self):
        return render_template("landingpage.html")

class CalorieCalculationPage(MethodView):

    def get(self):
        calculator_form = CalculatorForm()
        return render_template("calculator_page.html",calculatorform=calculator_form)

    def post(self):

        calculatorform = CalculatorForm(request.form)

        temperature_data = temperature.Temperature(country=calculatorform.country.data,
                                                   city=calculatorform.city.data)
        user_data = calorie.Calorie(age=float(calculatorform.age.data),
                                    weight=float(calculatorform.weight.data),
                                    height=float(calculatorform.height.data),
                                    temperature=temperature_data.get())
        return render_template("calculator_page.html",
                               result=True,
                               calculatorform=calculatorform,
                               calorie_output=user_data.calculate())

class CalculatorForm(Form):

    age = StringField("Age: ", default=27)
    weight = StringField("Weight: ",default=66)
    height = StringField("Height: ",default=177)
    country = StringField("Country: ",default="Turkey")
    city = StringField("City: ", default="Istanbul")

    button = SubmitField("Calculate")

app.add_url_rule("/", view_func=LandingPage.as_view("home_page")),
app.add_url_rule("/calories",view_func=CalorieCalculationPage.as_view("calc_page"))
app.run(debug=True)