import random
from logger import log_event
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    score = 0
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        score_text = pygame.font.Font(None, 36).render(f"Score: {Asteroid.score}", True, "white")
        screen.blit(score_text, (10, 10))

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, shot):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            Asteroid.score += 1
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        v1 = shot.velocity.rotate(random_angle)/shot.velocity.length() * self.velocity.length()
        v2 = shot.velocity.rotate(-random_angle)/shot.velocity.length() * self.velocity.length()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a2.velocity = v2