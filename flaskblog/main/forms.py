from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import  requests


class TemperatureForm(FlaskForm):
    city = StringField('City',validators=[DataRequired()])
    submit = SubmitField('Check')
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

    @staticmethod
    def fetch_temp_data(city_name):
        url = TemperatureForm.api_address+city_name
        json_data = requests.get(url).json()
        print (json_data)
        formated_data = int(json_data['main']['temp'])-273.15
        icon = json_data['weather'][0]['icon']
        print(formated_data, type(formated_data))
        return (formated_data,icon)