import random
import pygame

board_width = 128
board_height = 128 

pygame.init()
WIDTH, HEIGHT = 8*board_width, 8*board_height
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
running = True
bg = "#27187E"
primary = "#F38375"
secondary = "#717EC3"
speed_ratio = 8

cant_think_of_a_good_variable_name_so_its_time_for_a_really_really_really_terrible_variable_name_because_its_really_long = False
board_state = [[0 for i in range(board_width)] for i in range(board_height)]
board_state[board_height//2+1][board_width//2]=1
board_state[board_height//2-1][board_width//2]=1
board_state[board_height//2][board_width//2]=1
board_state[board_height//2][board_width//2-1]=1
board_state[board_height//2][board_width//2+1]=1

t=0

mouse_last_i = 0
mouse_last_j = -1

while running:
    t+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cant_think_of_a_good_variable_name_so_its_time_for_a_really_really_really_terrible_variable_name_because_its_really_long = not cant_think_of_a_good_variable_name_so_its_time_for_a_really_really_really_terrible_variable_name_because_its_really_long
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                new_board=[[board_state[i][j] for j in range(board_width)] for i in range(board_height)]
                for i in range(board_height):
                    for j in range(board_width):
                        alive_neighbours=0
                        tocheck = [
                            (i-1, j-1), (i-1, j  ), (i-1, j+1),
                            (i  , j-1),             (i  , j+1),
                            (i+1, j-1), (i+1, j  ), (i+1, j+1)
                        ]

                        for a, b in tocheck:
                            if(0<=a<board_height and 0<=b<board_width):
                                alive_neighbours+=1 if board_state[a][b] else 0
                        
                        if(board_state[i][j] and alive_neighbours not in [2, 3]):
                            new_board[i][j] = 0
                    
                        if(not board_state[i][j] and alive_neighbours in {3}):
                            new_board[i][j] = 1

                board_state = new_board

                # code reuse of all time

            elif event.key == pygame.K_BACKSPACE:
                board_state=[[0 for j in range(board_width)] for i in range(board_height)]

            elif event.key == pygame.K_ESCAPE:
                running = False
                continue

            elif event.key == pygame.K_KP_PLUS or event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                board_width+=1
                board_height+=1
                board_state.append([0 for i in range(board_width)])
                for i in range(board_height):
                    board_state[i].append(0)
                WIDTH, HEIGHT = 8*board_width, 8*board_height
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            elif event.key == pygame.K_MINUS:
                if(board_width>1 and board_height>1):
                    board_width-=1
                    board_height-=1
                    WIDTH, HEIGHT = 8*board_width, 8*board_height
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            elif event.key == pygame.K_r:
                board_state = [[0 for i in range(board_width)] for i in range(board_height)]
                board_state[board_height//2+1][board_width//2]=1
                board_state[board_height//2-1][board_width//2]=1
                board_state[board_height//2][board_width//2]=1
                board_state[board_height//2][board_width//2-1]=1
                board_state[board_height//2][board_width//2+1]=1

            elif event.key == pygame.K_RETURN:
                
                x, y = pygame.mouse.get_pos()
                i = x//8
                j = y//8
                board_state[i][j] = int(not board_state[i][j])

            elif event.key == pygame.K_f:
                speed_ratio = max(1, speed_ratio*0.5)

            elif event.key == pygame.K_s:
                speed_ratio = min(32, speed_ratio*2)

    buttons = pygame.mouse.get_pressed()
    if any(buttons):
        x, y = pygame.mouse.get_pos()
        i = x//24
        j = y//24
        if i!=mouse_last_i or j!=mouse_last_j and i<board_height and j<board_width:
            if buttons[0]:
                board_state[i][j] = 1
            else:
                board_state[i][j] = 0
            mouse_last_i = i
            mouse_last_j = j

    screen.fill(bg)

    for i in range(board_height):
        for j in range(board_width):
            if(board_state[i][j]):
                rect = pygame.Rect(8*i, 8*j, 8, 8)
                pygame.draw.rect(surface=screen, rect=rect, color=primary)

    if(t%speed_ratio==0 and cant_think_of_a_good_variable_name_so_its_time_for_a_really_really_really_terrible_variable_name_because_its_really_long):
        new_board=[[board_state[i][j] for j in range(board_width)] for i in range(board_height)]
        for i in range(board_height):
            for j in range(board_width):
                alive_neighbours=0
                tocheck = [
                    (i-1, j-1), (i-1, j  ), (i-1, j+1),
                    (i  , j-1),             (i  , j+1),
                    (i+1, j-1), (i+1, j  ), (i+1, j+1)
                ]

                for a, b in tocheck:
                    if(0<=a<board_height and 0<=b<board_width):
                        alive_neighbours+=1 if board_state[a][b] else 0
                
                if(board_state[i][j] and alive_neighbours not in [2, 3, 4, 5, 6, 7, 8]):
                    new_board[i][j] = 0

                if(not board_state[i][j] and alive_neighbours in {3, 4, 5, 6, 7, 8}):
                    new_board[i][j] = 1

        board_state = new_board

                
    pygame.display.flip()
    clock.tick(120)

pygame.quit()