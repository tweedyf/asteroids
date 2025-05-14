import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 100
	font = pygame.font.Font(None, 36)
	score = 0

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	# Create objects
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		screen.fill("black")

		score_text = font.render(f'Score: {score}', True, "white")
		screen.blit(score_text, (10, 10))

		for obj in asteroids:
			if player.collision(obj):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if shot.collision(obj):
					if obj.split() == 1:
						score += 1
					shot.kill()

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		# Limit fps to 60
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
