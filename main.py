from calorie import Calorie
from temperature import Temperature

temperature_object = Temperature("USA", "San Francisco").get()
calorie_object = Calorie(70, 175, 32, temperature_object).calculate()
print(calorie_object)

