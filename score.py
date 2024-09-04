import pygame

class Score():
    def __init__(self):
        self.__score = 0
    
    def get_score(self):
        return self.__score

    def add_points(self, radius):
        if radius == 20:
            self.__score += 40
        if radius == 40:
            self.__score += 20
        if radius == 60:
            self.__score += 10

