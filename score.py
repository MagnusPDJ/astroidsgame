import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()   

        self.__score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 25)
        self.text = self.font.render(f"Score: {self.get_score()}", True, "white")
        self.__textrect = self.text.get_rect()
        self.__textrect.center = (75, 30)
    
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
        screen.blit(self.text, self.__textrect)
    
    def update(self, dt):
        self.text = self.font.render(f"Score: {self.get_score()}", True, "white")
