# 11-1 unittest practise

def city_country (city,country,population=''):
    if population:
        city_country_variable = city + ',' + country + '-' + population
    else:
        city_country_variable = city + ',' + country
    return (city_country_variable.title())

city_country('selangor','malaysia')

import unittest

class CityTestCase (unittest.TestCase):
    
    def test_city_country (self):
        show_city_country = city_country('selangor','malaysia')
        self.assertEqual(show_city_country, "Selangor,Malaysia")
    
    def test_city_country_population(self):
        show_city_country = city_country('selangor','malaysia','2000000')
        self.assertEqual(show_city_country, "Selangor,Malaysia-2000000")

unittest.main()