from bs4 import BeautifulSoup as bs
import requests

class CalcCalories:
    """ class calculate BMR(Basal Metabolic Rate)
    formula: BRM = 10*weight + 6.25*height - 5*age + 5 -10*temperature"""

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        bmr = 10 * float(self.weight) + 6.25*float(self.height) -5 * float(self.age) + 5 - 10 * float(self.temperature)
        return bmr

class Temperature:
    """class that get a temperature from website https://www.timeanddate.com/weather for inputed country/city"""

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def scrape_temp(self):
        # set variable to 0
        temp = 0
        # generating url for each country / city
        url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
        # get response
        response = requests.get(url)
        soup = bs(response.content, features='html.parser')
        # finding correct tag
        result = soup.find_all('div', {'class': 'h2'})
        for i in result:
            # converting into int, riping of celsius symbol
            temp += float(i.get_text().replace('°C', ''))
        return temp
