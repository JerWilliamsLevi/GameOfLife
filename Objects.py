# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:02:16 2023

@author: Jerle
"""

class player:
    def __init__(self, name, player, age, gender, money, retirement, car1):
        self.name = 'name'
        self.player = 0
        self.age = 16
        self.gender = 0;
        self.money = 0
        self.retirement = 0
        self.car1 = car(0,0,0,0)
        
    def buy_car(self, spending, car_type):
        car_cost = 0
        if car_type == 0:
            car_cost = 3000
        elif car_type == 1:
            car_cost = 10000
        elif car_type == 2:
            car_cost = 30000
        if self.money > car_cost:
            self.money = self.money - car_cost
            if car_type == 2:
                self.car1.rvalue = car_cost - 5000
            else:
                self.car1.rvalue = car_cost
            self.car1.irepairs = 0;
            self.car1.brunning = True
            
    def buy_house():
        pass
    def have_child():
        pass
    def get_job():
        pass
    def quit_job():
        pass
class vehicle:
    pass
class house:
    pass
class car:
    def __init__(self, irepairs, rvalue, brunning, car_type):
        self.irepairs = 0
        self.rvalue = 0.0
        self.brunning = False
    def repair(self):
        pass
    def drive():
        pass
    def check_status():
        pass
class child:
    pass