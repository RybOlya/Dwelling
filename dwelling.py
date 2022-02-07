import datetime
from typing import Union
from typing import List
class InfrastructureProximity:
    def __init__(self, school, kindergarden, groceries, pharmacy, gym, leisure_centre) -> None:
        self.school = school
        self.kindergarden = kindergarden
        self.groceries = groceries
        self.pharmacy = pharmacy
        self.gym = gym
        self.leisure_centre = leisure_centre
class DwellingInfo:
    def __init__(self, name, location, area, price_per_square_meter, air_quality, bedrooms, 
                parking,heating, state_of_dwelling,security, school, kindergarden, groceries,
                pharmacy, gym, leisure_centre) -> None:
        self.name = name
        self.location = location
        self.area = area
        self.price_per_square_meter = price_per_square_meter
        self.air_quality = air_quality
        self.bedrooms = bedrooms
        self.parking = parking
        self.heating = heating
        self.state_of_dwelling = state_of_dwelling
        self.security = security
        self.infrastructure = InfrastructureProximity( school, kindergarden, groceries, pharmacy,
                                                       gym, leisure_centre)
class ApartmentType(DwellingInfo):
    def __init__(self, name, location, area, price_per_square_meter, air_quality, bedrooms, parking,
                 heating, state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym,
                  leisure_centre, dwelling_class, number_of_storeys, elevator,concierge) -> None:
        super().__init__(name, location, area, price_per_square_meter, air_quality, bedrooms, parking,
                         heating, state_of_dwelling, security, school, kindergarden, groceries, pharmacy,
                         gym, leisure_centre)
        self.dwelling_class = dwelling_class
        self.number_of_storeys = number_of_storeys
        self.elevator = elevator
        self.concierge = concierge
class PentHouse(ApartmentType):
    def __init__(self, name, location, area, price_per_square_meter, air_quality, bedrooms, parking, 
                 heating, state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym,
                 leisure_centre, dwelling_class, number_of_storeys, elevator, concierge, private_rooftop) -> None:
        super().__init__(name, location, area, price_per_square_meter, air_quality, bedrooms, parking,
                         heating, state_of_dwelling, security, school, kindergarden, groceries, pharmacy, 
                         gym, leisure_centre, dwelling_class, number_of_storeys, elevator, concierge)
        self.private_rooftop = private_rooftop
class Studio(ApartmentType):
    def __init__(self, name, location, area, price_per_square_meter, air_quality, bedrooms, parking, heating, 
                 state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym, leisure_centre, 
                 dwelling_class, number_of_storeys, elevator, concierge) -> None:
        super().__init__(name, location, area, price_per_square_meter, air_quality, bedrooms, parking, heating, 
                         state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym, leisure_centre, 
                         dwelling_class, number_of_storeys, elevator, concierge)
class ManorType(DwellingInfo):
    def __init__(self, name, location, area, price_per_square_meter, air_quality, bedrooms, parking, heating,
                 state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym, leisure_centre, 
                 private_plot_area_in_acres, floors) -> None:
        super().__init__(name, location, area, price_per_square_meter, air_quality, bedrooms, parking, heating, 
                         state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym, leisure_centre)
        self.private_plot_area_in_acres = private_plot_area_in_acres
        self.floors = floors
class DetachedHouse(ManorType):
    def __init__(self, name, location, area, price_per_square_meter, air_quality, bedrooms, parking, heating, 
                 state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym, leisure_centre, 
                 private_plot_area_in_acres, floors, additional_premises) -> None:
        super().__init__(name, location, area, price_per_square_meter, air_quality, bedrooms, parking, heating,
                         state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym, leisure_centre,
                         private_plot_area_in_acres, floors)
        self.additional_premises = additional_premises
class TownHouse(ManorType):
    def __init__(self, name, location, area, price_per_square_meter, air_quality, bedrooms, parking, heating, 
                 state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym, leisure_centre, 
                 private_plot_area_in_acres, floors, houses_quantity) -> None:
        super().__init__(name, location, area, price_per_square_meter, air_quality, bedrooms, parking, heating,
                         state_of_dwelling, security, school, kindergarden, groceries, pharmacy, gym, leisure_centre, 
                         private_plot_area_in_acres, floors)
        self.houses_quantity = houses_quantity
if __name__ == '__main__':
    townhouse_privesin = TownHouse("Провесінь","вул. Тракт Глинянський, 152",181,31000,33,3,True,"газовий котел", "без ремонту",False, 300, 300, 210, 300, 500, 700, 8,1,29)

    #apartment_on_yaroslavenka = Studio("Swiss Villa", "23 Yaroslavenka St.",50,30000,15,2,True, "individual", "turnkey",True,)