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
class RealEstateAgency(DwellingInfo):
    all_dwellings = []
    apartments = []
    manors = []
    def add_dwelling(new_dwelling)->None:
        RealEstateAgency.all_dwellings.append(new_dwelling)
        print(new_dwelling.name, " додано")
    def show_available_dwellings()->None:
        for dwellings_available in RealEstateAgency.all_dwellings: 
            print(dwellings_available.name," в каталозі")
    
    def get_dwellings_sorted_by_price()->List[Union[str,float]]:
        ch = input("Сортування за ціною:\n 1.За зростанням\n 2.За спаданням\n Виберіть 1 або 2:  ")
        if ch is "1":
            sorted_dwelling = sorted(RealEstateAgency.all_dwellings, key = lambda d: d.price_per_square_meter)  
        elif ch is "2":
            sorted_dwelling = sorted(RealEstateAgency.all_dwellings, key = lambda d: d.price_per_square_meter, reverse=True)  

        for dwelling in sorted_dwelling:
            print(dwelling.name, dwelling.price_per_square_meter)
        return (list[dwelling.name, dwelling.price_per_square_meter])
    
        
    def get_dwellings_sorted_by_location()->List[Union[str,float]]:
        ch = input("Локації за алфавітом:\n Виберіть (yes/no):")
        if ch == "yes":
            sorted_dwelling = sorted(RealEstateAgency.all_dwellings, key = lambda d: d.location)  
        elif ch == "no":
            sorted_dwelling = sorted(RealEstateAgency.all_dwellings, key = lambda d: d.location, reverse=True)  

        for dwelling in sorted_dwelling:
            print(dwelling.name," на ", dwelling.location)
        return (list[dwelling.name, dwelling.price_per_square_meter])
if __name__ == '__main__':
    apartment_on_stusa = Studio("ЖБ на Стуса", "вул. Стуса, 39", 100, 30000, 31, 2, True, "індивідуальне", "зданий в експлуатацію", True, 800, 200, 200, 500, 500, 100, "бізнес", 9, True, True)
    apartment_on_yaroslavenka = PentHouse("Вілла Швейцарія", "вул. Ярославенка, 21",90,30000,15,2,True, "індивідуальне", "зданий в експлуатацію",True, 200, 100, 50, 50, 800, 100, "комфорт", 5, True, True, True)
    cottage_timberland = DetachedHouse("КМ TIMBERLAND", "вул. Лисеницька, 66", 190,28000, 0,3,True, "газовий котел", "з чорновим ремонтом",True, 300, 200, 300, 500, 400, 800, 1.5, 2,False)
    townhouse_privesin = TownHouse("Провесінь","вул. Тракт Глинянський, 152",181,31000,33,3,True,"газовий котел", "без ремонту",False, 300, 300, 210, 300, 500, 700, 8,1,29) 
    RealEstateAgency.add_dwelling(apartment_on_stusa)
    RealEstateAgency.add_dwelling(apartment_on_yaroslavenka)
    RealEstateAgency.add_dwelling(cottage_timberland)
    RealEstateAgency.add_dwelling(townhouse_privesin)
    RealEstateAgency.show_available_dwellings()
    RealEstateAgency.get_dwellings_sorted_by_price()
    RealEstateAgency.get_dwellings_sorted_by_location()
