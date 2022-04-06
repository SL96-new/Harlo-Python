# 9-1,2.4 create Class (restaurant)
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print ("\n" + self.restaurant_name.title() + " is a " + self.cuisine_type + " restaurant")

    def open_restaurant(self):
        print ("It is opening now!")
    
    def number_served(self):
        print ("This restaurant have served " + str(self.number_served) + " people.")
    
    def set_number_served (self,number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print ("You can't descrease number of people served!")

    def increment_number_served(self, number_increment):
        if number_increment >= 0:
            self.number_served += number_increment
        else:
            print ("There are no decreases in number of people served!")
        

sushi_mentai = Restaurant("sushi mentai","Japanese")
sushi_mentai.describe_restaurant()
sushi_mentai.open_restaurant()
sushi_mentai.set_number_served(2500)
sushi_mentai.number_served()
sushi_mentai.increment_number_served (52)
sushi_mentai.number_served()

twopesos = Restaurant ("two pesos","steamboat")
twopesos.describe_restaurant()
twopesos.open_restaurant()
