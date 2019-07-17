#类
class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served =0

    def describe_restaurant(self):
        print(self.restaurant_name+self.cuisine_type+str(self.number_served))

    def open_restaurant(self):
        print("the restaurant is open")

    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self):
        self.number_served+=100




#my_restaurant=Restaurant("happy-restaurant","coffee")
#your_restaurant=Restaurant("zixu-restayrant","rice")
#print(my_restaurant.restaurant_name+my_restaurant.cuisine_type)
#my_restaurant.set_number_served(200)
#my_restaurant.increment_number_served()
#my_restaurant.describe_restaurant()
#your_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()