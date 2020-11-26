import random
import pygame
from pygame.math import Vector2
import LED_display as LMD
import threading

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

pygame.init()

FONT = pygame.font.SysFont('Helvetica', 25)
FPS = 30
WIN_WIDTH = 640
WIN_HEIGHT = 320
MAX_SCORE = 5
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (64, 64, 64)


class Ball(pygame.sprite.Sprite):

       def __init__(self, width, height):
           super().__init__()
           self.width, self.height = width, height
           self.image = pygame.Surface([10, 10])
           self.image.fill(WHITE)
           self.rect = self.image.get_rect()
           self.initialize()

       def initialize(self):
           """Reset the attributes of the ball for a restart.

           Called when the ball leaves the screen and a player scores.
           """
           self.direction = random.choice(
               [Vector2(-10, -10), Vector2(10, -10),
                Vector2(-10, 10), Vector2(10, 10)])
           self.position = Vector2(WIN_WIDTH/2, WIN_HEIGHT/2)
           self.rect.center = self.position
           self.hits = 0
           self.speed_up = 1.0

       def hit(self):
           self.hits += 1
           self.speed_up = 1.0 + self.hits/10

       def update(self):
           if self.position.y <= 10:  # upper border
               self.direction = random.choice([Vector2(-10, 10), Vector2(10, 10)])
           if self.position.y >= self.height - 10:  # bottom border
               self.direction = random.choice([Vector2(-10, -10), Vector2(10, -10)])

           self.position += self.direction * self.speed_up
           self.rect.center = self.position


class Player(pygame.sprite.Sprite):

       def __init__(self, side, width, height):
           super().__init__()
           self.score = 0
           self.width, self.height = width, height
           self.racket_height = 100
           self.movement_speed = 20
           offset = 20
           self.image = pygame.Surface([10, self.racket_height])
           self.image.fill(WHITE)

           if side == 'Left':
               self.position = Vector2(offset, self.height/2)
           else:
               self.position = Vector2(self.width-offset-10, self.height/2)
           self.rect = self.image.get_rect(topleft=self.position)

       def move_up(self):
           if self.position.y > 0:
               self.position.y -= self.movement_speed
               self.rect.top = self.position.y

       def move_down(self):
           if self.position.y + self.racket_height < self.height:
               self.position.y += self.movement_speed
               self.rect.top = self.position.y


def game_over(screen, winner, left_paper, right_player):
       gray_overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
       gray_overlay.fill(GRAY)
       gray_overlay.set_colorkey(GRAY)
       pygame.draw.rect(gray_overlay, BLACK, [0, 0, WIN_WIDTH, WIN_HEIGHT])
       gray_overlay.set_alpha(99)
       screen.blit(gray_overlay, (0, 0))
       font = pygame.font.SysFont(None, 100)
       game_over = font.render('{} Player WINS!'.format(winner), True, WHITE)
       screen.blit(game_over, (WIN_WIDTH / 2 - 300, WIN_HEIGHT / 2 - 100))
       scoreline = font.render(
           '{} - {}'.format(left_paper.score, right_player.score), True, WHITE)
       screen.blit(scoreline, (WIN_WIDTH / 2 - 50, WIN_HEIGHT / 2 + 100))
       pygame.display.update()
       pygame.time.delay(2000)


def render_score(left_player, right_player, font):
       """Render player scores onto surfaces."""
       left_player_score = font.render(str(left_player.score), True, (255, 255, 255))
       right_player_score = font.render(str(right_player.score), True, (255, 255, 255))
       return left_player_score, right_player_score


def main():
       screen = pygame.display.set_mode(DISPLAY, 0, 32)
       clock = pygame.time.Clock()

       left_player = Player('Left', WIN_WIDTH, WIN_HEIGHT)
       right_player = Player('Right', WIN_WIDTH, WIN_HEIGHT)
       curr_ball = Ball(WIN_WIDTH, WIN_HEIGHT)

       all_sprites = pygame.sprite.Group(left_player, right_player, curr_ball)

       goal_text = FONT.render(str(MAX_SCORE), True, (255, 255, 0))
       left_player_score, right_player_score = render_score(
           left_player, right_player, FONT)

       done = False

       while not done:
           # Event handling.
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   done = True

           keys = pygame.key.get_pressed()
           if keys[pygame.K_q]:
               done = True
           if keys[pygame.K_UP]:
               right_player.move_up()
           if keys[pygame.K_DOWN]:
               right_player.move_down()
           if keys[pygame.K_w]:
               left_player.move_up()
           if keys[pygame.K_s]:
               left_player.move_down()

           # Game logic.
           all_sprites.update()
           # Determine winner.
           if left_player.score >= MAX_SCORE or right_player.score >= MAX_SCORE:
               # This is a conditional expression (similar
               # to a ternary in other languages).
               winner = 'Left' if left_player.score > right_player.score else 'Right'
               game_over(screen, winner, left_player, right_player)
               done = True

           # Collision detection with the rackets/players.
           col_left = curr_ball.rect.colliderect(left_player.rect)
           col_right = curr_ball.rect.colliderect(right_player.rect)
           if col_right or col_left:
               curr_ball.direction.x *= -1  # Reverse the x component of the vectow.
               curr_ball.hit()

           if curr_ball.rect.x <= 0:  # left border
               right_player.score += 1
               curr_ball.initialize()
               left_player_score, right_player_score = render_score(
                   left_player, right_player, FONT)
           elif curr_ball.rect.x >= WIN_WIDTH:  # right border
               left_player.score += 1
               curr_ball.initialize()
               left_player_score, right_player_score = render_score(
                   left_player, right_player, FONT)

           # Drawing.
           screen.fill((30, 30, 70))
           screen.blit(left_player_score, (WIN_WIDTH / 2 - 100, 10))
           screen.blit(right_player_score, (WIN_WIDTH / 2 + 100, 10))
           screen.blit(goal_text, (WIN_WIDTH / 2, 0))
           all_sprites.draw(screen)

           pygame.display.set_caption('Ping Pong {}'.format(clock.get_fps()))

           pygame.display.flip()
           clock.tick(FPS)


if __name__ == '__main__':
       LED_init()
       main()
       pygame.quit()
