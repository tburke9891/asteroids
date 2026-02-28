import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS, 
    LINE_WIDTH, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED, 
    PLAYER_SHOOT_SPEED, 
    PLAYER_SHOOT_COOLDOWN_SECONDS,
   )
from shot import Shot


class Player(CircleShape):
    containers = () # This will be set to the groups that hold Player instances in main.py
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.line_width = LINE_WIDTH
        self.rotation = 0
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right

      # print(f"Triangle points: {a}, {b}, {c}")
      return [(int(a.x), int(a.y)), (int(b.x), int(b.y)), (int(c.x), int(c.y))]
    
    def draw(self, screen):
      pygame.draw.polygon(surface = screen, color = "white", points = self.triangle(), width = self.line_width) # Draw the player as a triangle

    def rotate(self, dt):
      self.rotation += PLAYER_TURN_SPEED * dt # Rotate the player based on turn speed and delta time  

    def update(self, dt):
      keys = pygame.key.get_pressed()
      self.shot_cooldown -= dt # Decrease the shot cooldown by delta time

      if keys[pygame.K_a]:
          self.rotate(-dt) # Rotate left (counter-clockwise)
      if keys[pygame.K_d]:
          self.rotate(dt) # Rotate right (clockwise)
      if keys[pygame.K_w]:
          self.move(dt) # Move forward
      if keys[pygame.K_s]:
          self.move(-dt) # Move backward
      if keys[pygame.K_SPACE] and self.shot_cooldown <= 0:
          self.shoot() # Shoot your shot
          self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS # Reset the shot cooldown
    
    def move(self, dt):
       unit_vector = pygame.Vector2(0, 1)
       rotated_vector = unit_vector.rotate(self.rotation)
       rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
       self.position += rotated_with_speed_vector

    def shoot(self):
        """Create a new Shot instance that starts at the player's position and moves in the direction the player is facing.
        """
        shot = Shot(x = self.position.x, y = self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


