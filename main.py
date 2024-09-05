import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score


def main():
    print("Starting asteroids!")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")
    
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
    print(score.get_score())
    print(score.draw(screen))

    while True: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for update in updatable:
            update.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game over!")
                print(f"Your score was: {score.get_score()}!")
                exit()
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
    main()
