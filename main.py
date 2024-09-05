import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score


def main():

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    pygame.display.quit()
    pygame.display.set_caption("Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Score.containers = (updatable, drawable)

    asteroidfield = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    score = Score()

    while True: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        for update in updatable:
            update.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
#                print("Game over!")
#                print(f"Your score was: {score.get_score()}!")
#                exit()
                score.endscreen(screen)
                pygame.display.update() 
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if pygame.key.name(event.key) == "n":
                                print("Goodbye")
                                exit()
                            if pygame.key.name(event.key) == "y":
                                main()

            for shot in shots:
                if asteroid.check_for_collision(shot):
                    shot.kill()
                    asteroid.split()
                    score.add_points(asteroid.radius)

        screen.fill((0,0,0))        

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    print("Starting asteroids!")
    main()
