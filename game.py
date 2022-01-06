import pygame
import time
import random

pygame.init()

width=1200
height=600

window=pygame.display.set_mode((width,height))
pygame.display.update()

pygame.display.set_caption("Snake Game")

red = (255,0,145)
green = (5,236,128)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

bg = pygame.image.load('back.jpeg')
bg = pygame.transform.scale(bg,(1200, 600))

snake_circle = 17
my_snake = []
count=0

clock=pygame.time.Clock()
snake_speed = 17

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 10)

def draw_snake(lenght_snake, my_snake):

    if len(my_snake) > lenght_snake:
        del my_snake[-1]

    for el in range(0, len(my_snake)):
        if el != 0:
            pygame.draw.rect(window, black, (my_snake[el][0],my_snake[el][1],snake_circle,snake_circle))
            pygame.draw.rect(window, green, (my_snake[el][0],my_snake[el][1],snake_circle,snake_circle), 1, border_radius=1 )
        else:
            pygame.draw.rect(window, green, (my_snake[el][0],my_snake[el][1],snake_circle,snake_circle))

        

def message(msg, color):

    msg = font_style.render(msg,True, color)
    window.blit(msg, [width/2 - 300, height/2 - 50])

def show_score(score, color):

    msg = font_style.render("Score: " + str(score),True, color)
    window.blit(msg, [10, 10])


def gameloop():

    game_over=False
    game_close=False
    score=0

    x1=width/2
    y1=height/2

    x1_change=0
    y1_change=0
    
    my_snake = [[x1,y1]]
    lenght_snake = 1

    foodx = round(random.randrange(0, width-snake_circle))
    foody = round(random.randrange(0, height-snake_circle))

    while game_close == False:
        while game_over == True:
            window.fill(black)
            message("You Lost. Press Q to quit or C to play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame .KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True

                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close=True
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_circle
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_circle
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_circle
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_circle
        
        if x1 >= width+10 or x1 < -20 or y1 >= height-10 or y1 < 0+10:
            game_over=True

        x1 = x1 + x1_change
        y1 = y1 + y1_change

        window.blit(bg, (0, 0))
        show_score(score, red)

        
        my_snake.insert(0, [x1,y1])

        draw_snake(lenght_snake, my_snake)
        for i in range(1,len(my_snake)):
            if my_snake[0][0] == my_snake[i][0] and my_snake[0][1] == my_snake[i][1]:
                game_over=True

        pygame.draw.circle(window, red, [foodx,foody],snake_circle-8)
        pygame.display.update()


        if (x1>foodx-25 and x1<foodx+10) and (y1>foody-25 and y1<foody+10):
            foodx = round(random.randrange(10, width-15-snake_circle))
            foody = round(random.randrange(-10, height+15-snake_circle))
            lenght_snake +=1
            score+=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameloop()