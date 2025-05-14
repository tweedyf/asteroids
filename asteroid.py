import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return 1
		else:
			random_angle = random.uniform(20,50)
			ast_1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
			ast_2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
			ast_1.velocity = self.velocity.rotate(random_angle) * 1.2
			ast_2.velocity = self.velocity.rotate(-1 * random_angle) * 1.2
			return 0
