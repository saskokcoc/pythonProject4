import random
class Human:
    def __init__(self, name="Альбердо", job = None, home = None, car = None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.glabhess = 50
        self.stiety = 50
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clear_home(self):
        pass
    def to_repair(self):
        pass
    def days_indexrs(self, day):
        pass
    def is_alive(self):
        pass
    def live(self, day):
        pass
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.kin = brand_list[self.brand]['kin']
        self.consumpion = brand_list[self.brand]['consumpion']
brands_of_cars ={'BMW':{'fuel':100, "kin":240,"consumpion":260}},
                {'лада':{'fuel'{:67, "kin":120,"consumpion":120}},
                {'хламідія':{'fuel':98, "kin":160,"consumpion":164}}
