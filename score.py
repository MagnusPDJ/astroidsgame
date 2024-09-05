import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()   

        self.__score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 25)
        self.text1 = self.font.render(f"Score: {self.get_score()}", True, "white")
        self.__textrect1 = self.text1.get_rect()
        self.__textrect1.center = (75, 30)
        self.text2 = self.font.render(f"Game Over! Try again? (y / n)", True, "white")
        self.__textrect2 = self.text2.get_rect()
        self.__textrect2.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    def get_score(self):
        return self.__score

    def add_points(self, radius):
        if radius == 20:
            self.__score += 40
        if radius == 40:
            self.__score += 20
        if radius == 60:
            self.__score += 10
    def draw(self, screen):
        screen.blit(self.text1, self.__textrect1)
    
    def update(self, dt):
        self.text1 = self.font.render(f"Score: {self.get_score()}", True, "white")

    def endscreen(self, screen):
        screen.blit(self.text2, self.__textrect2)
