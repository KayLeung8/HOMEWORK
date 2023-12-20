#4.1
class Planet:
    distance_sun_to_earth = 147000000

    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        distance_to_earth = abs(self.distance_from_sun - self.distance_sun_to_earth)
        return {'distance_to_earth': distance_to_earth}


planetA = Planet(name='PlanetA', distance_from_sun=148000000, planet_type='Terrestrial')
mars = Planet(name='Mars', distance_from_sun=225000000, planet_type='Terrestrial')

distance_earth_planetA = planetA.get_distance_to_earth()
distance_earth_mars = mars.get_distance_to_earth()
print(f"{planetA.name} is {distance_earth_planetA['distance_to_earth']} kilometres away from Earth.")
print(f"{mars.name} is {distance_earth_mars['distance_to_earth']} kilometres away from Earth.")


#4.2
class Mercury(Planet):
    orbit_days = 88

    def __init__(self, name='Mercury', distance_from_sun=58000000, planet_type='Terrestrial'):
        super().__init__(name, distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
        print(f"Happy New Year on Mercury! A year on Mercury lasts {Mercury.orbit_days} Earth days.")

mercury = Mercury()
print(f"Name: {mercury.name}")
print(f"Distance from Sun: {mercury.distance_from_sun} kilometres")
print(f"Planet Type: {mercury.planet_type}")
distance_earth_mercury = mercury.get_distance_to_earth()
print(f"Distance to Earth: {distance_earth_mercury['distance_to_earth']} kilometres")
Mercury.happy_new_year()


#4.3
class Jupiter(Planet):
    orbit_days = 4383

    def __init__(self, name='Jupiter', distance_from_sun=779000000, planet_type='Gas Giant', number_of_moons=80):
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        print(f"Happy New Year on Jupiter! A year on Jupiter lasts {Jupiter.orbit_days} Earth days.")


jupiter = Jupiter()
print(f"Name: {jupiter.name}")
print(f"Distance from Sun: {jupiter.distance_from_sun} kilometres")
print(f"Planet Type: {jupiter.planet_type}")
print(f"Number of Moons: {jupiter.number_of_moons}")
distance_earth_jupiter = jupiter.get_distance_to_earth()
print(f"Distance to Earth: {distance_earth_jupiter['distance_to_earth']} kilometres")
Jupiter.happy_new_year()
