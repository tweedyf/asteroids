import pygame
from constants import *
from circleshape import *
from player import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 100
#	print("Starting Asteroids!")
#	print(f"Screen width: {SCREEN_WIDTH}")
#	print(f"Screen height: {SCREEN_HEIGHT}")

	# Create player
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
#	Player.containers = (drawable, updatable)
	drawable.add(player)
	updatable.add(player)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		updatable.update(dt)
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
