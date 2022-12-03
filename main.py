""" TODO: when snake has length, we need to store it's coordinates somehow
to check for collissions of the whole thing so that food doesn't spawn in there """
# fix^ store position of each segment as a tuple in a list like this ((x,y),(x,y))
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

BACKGROUND = (125, 125, 125)
FOOD_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

FPS = 10

SNAKE_BLOCK = 10

font = pygame.font.SysFont("Ubuntu", 25)
font_score = pygame.font.SysFont("Ubuntu", 35)


class Snake:
    pos_x = 0
    pos_y = 0
    width = 10
    height = 10
    length = 1
    # speed = 1
    color = (255, 255, 255)

    def __init__(self, position_x: int, position_y: int, width: int, height: int, length: int, color: int):
        self.pos_x = position_x
        self.pos_y = position_y
        self.width = width
        self.height = height
        self.length = length
        # self.speed = speed
        self.color = color


def whole_snake(snake_block, snake_list):
    for s in snake_list:
        pygame.draw.rect(SURFACE, SNAKE_COLOR, [
                         s[0], s[1], snake_block, snake_block])


def collissions(x_1, y_1, x_2, y_2):
    if x_1 == x_2 and y_1 == y_2:
        return True
    return False


def main():
    clock = pygame.time.Clock()
    Player = Snake(WIDTH/2 - SNAKE_BLOCK, HEIGHT/2 - SNAKE_BLOCK,
                   SNAKE_BLOCK, SNAKE_BLOCK, 1, SNAKE_COLOR)
    snake_list = []
    is_food_on = False
    lost = False
    direction = 0
    while True:
        if lost:
            pass
        # lock fps
        clock.tick(FPS)
        # draw background
        SURFACE.fill(BACKGROUND)
        # if food isn't already on screen, calculate it's coordinates
        if not is_food_on:
            while not is_food_on:
                food_pos_x = round(random.randrange(0, WIDTH)/10)*10
                food_pos_y = round(random.randrange(0, HEIGHT)/10)*10
                # if food isn't spawned inside snake then food is on screen and we get out of the loop
                if food_pos_x != Player.pos_x and food_pos_y != Player.pos_y:
                    is_food_on = True
                    break

        # draw food on screen
        pygame.draw.rect(SURFACE, FOOD_COLOR, [
                         food_pos_x, food_pos_y, SNAKE_BLOCK, SNAKE_BLOCK])
        # read keyboard input
        pygame.event.pump()
        # save keyboard input
        keys = pygame.key.get_pressed()
        # check for quit
        if keys[pygame.K_q]:
            pygame.quit()
        snake_head = []
        snake_head.append(Player.pos_x)
        snake_head.append(Player.pos_y)
        snake_list.append(snake_head)
        # checks if snake_list is longer than snake length, and deletes the first element
        if len(snake_list) > Player.length:
            del snake_list[0]
        # checks the snake_list, if it has same coordinates as snake head, lose game
        for x in snake_list[:-1]:
            if x == snake_head:
                lost = True
        # draw snake on screen
        whole_snake(SNAKE_BLOCK, snake_list)
        #pygame.draw.rect(SURFACE, Player.color, pygame.Rect(Player.pos_x, Player.pos_y, Player.width, Player.height))

        # check which key was pressed, change snake movement to that direction
        if keys[pygame.K_UP] and direction != 1:
            direction = 0
        if keys[pygame.K_DOWN] and direction != 0:
            direction = 1
        if keys[pygame.K_LEFT] and direction != 3:
            direction = 2
        if keys[pygame.K_RIGHT] and direction != 2:
            direction = 3

        # move snake in direction check
        if direction == 0:
            Player.pos_y -= 10
        if direction == 1:
            Player.pos_y += 10
        if direction == 2:
            Player.pos_x -= 10
        if direction == 3:
            Player.pos_x += 10

        # check collisions for map bounds
        if Player.pos_x > WIDTH - Player.width:
            Player.pos_x = 0
        if Player.pos_x < 0:
            Player.pos_x = WIDTH - Player.width
        if Player.pos_y > HEIGHT - Player.height:
            Player.pos_y = 0
        if Player.pos_y < 0:
            Player.pos_y = HEIGHT - Player.height

        # check collisions for food
        if collissions(Player.pos_x, Player.pos_y, food_pos_x, food_pos_y):
            Player.length += 1
            is_food_on = False
            pygame.display.flip()

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
