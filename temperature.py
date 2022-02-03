import requests
from selectorlib import Extractor

class Temperature:

    """Represent a temperature value extracted from timeanddate.com/weather"""

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def get(self):
        url = "http://www.timeanddate.com/weather/" + str(self.country).lower() + "/" + str(self.city).lower()
        req_object = requests.get(url).text
        extractor = Extractor.from_yaml_file("temperature.yaml")
        raw_result = extractor.extract(req_object)
        return float(raw_result["temp"].replace(" °C",""))
