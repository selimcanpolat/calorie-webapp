from calorie import Calorie
from temperature import Temperature

if __name__ == "__main__":
    temperature_object = Temperature("USA", "San Francisco").get()
    calorie_object = Calorie(70, 175, 32, temperature_object).calculate()
    print(calorie_object)

