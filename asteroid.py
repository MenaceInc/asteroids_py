from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        first_asteroid_vel = self.velocity.rotate(angle)
        second_asteroid_vel = self.velocity.rotate(-angle)

        first = Asteroid(self.position[0], self.position[1], (self.radius - ASTEROID_MIN_RADIUS))
        first.velocity = first_asteroid_vel * 1.2
        second = Asteroid(self.position[0], self.position[1], (self.radius - ASTEROID_MIN_RADIUS))
        second.velocity = second_asteroid_vel * 1.2