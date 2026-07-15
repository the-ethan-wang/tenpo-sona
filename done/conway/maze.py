import random
import pygame

board_width = 50
board_height = 50 

pygame.init()
WIDTH, HEIGHT = 16*board_width, 16*board_height
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
running = True
bg = "#27187E"
primary = "#F38375"
secondary = "#717EC3"
speed_ratio = 8

cant_think_of_a_good_variable_name_so_its_time_for_a_really_really_really_terrible_variable_name_because_its_really_long_hmm_im_really_bored_and_its_an_unusually_late_hour_of_the_night_so_i_feel_like_adding_more_to_this_really_really_really_really_really_really_really_really_really_long_variable_name_we_should_add_more_to_this_how_about_some_pi_3_1415926535897273238462643383279533846264338327950_idk_if_that_was_right_cuz_i_havent_checked_in_a_long_time_also_if_you_know_more_feel_free_to_submit_a_pull_request_first_you_fork_the_repository_then_make_edits_and_commits_and_then_click_the_contribute_or_create_a_pull_request_its_usually_a_big_big_green_red_button_very_clickable_so_you_just_click_that_and_click_submit_pull_request_then_if_its_right_i_might_accept_thanks_lol = True
board_state = [[random.choice([0, 0, 0, 0, 0, 0, 0, 1]) for i in range(board_width)] for i in range(board_height)]
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
                cant_think_of_a_good_variable_name_so_its_time_for_a_really_really_really_terrible_variable_name_because_its_really_long_hmm_im_really_bored_and_its_an_unusually_late_hour_of_the_night_so_i_feel_like_adding_more_to_this_really_really_really_really_really_really_really_really_really_long_variable_name_we_should_add_more_to_this_how_about_some_pi_3_1415926535897273238462643383279533846264338327950_idk_if_that_was_right_cuz_i_havent_checked_in_a_long_time_also_if_you_know_more_feel_free_to_submit_a_pull_request_first_you_fork_the_repository_then_make_edits_and_commits_and_then_click_the_contribute_or_create_a_pull_request_its_usually_a_big_big_green_red_button_very_clickable_so_you_just_click_that_and_click_submit_pull_request_then_if_its_right_i_might_accept_thanks_lol = not cant_think_of_a_good_variable_name_so_its_time_for_a_really_really_really_terrible_variable_name_because_its_really_long_hmm_im_really_bored_and_its_an_unusually_late_hour_of_the_night_so_i_feel_like_adding_more_to_this_really_really_really_really_really_really_really_really_really_long_variable_name_we_should_add_more_to_this_how_about_some_pi_3_1415926535897273238462643383279533846264338327950_idk_if_that_was_right_cuz_i_havent_checked_in_a_long_time_also_if_you_know_more_feel_free_to_submit_a_pull_request_first_you_fork_the_repository_then_make_edits_and_commits_and_then_click_the_contribute_or_create_a_pull_request_its_usually_a_big_big_green_red_button_very_clickable_so_you_just_click_that_and_click_submit_pull_request_then_if_its_right_i_might_accept_thanks_lol
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

                # code reuse of all time (im too tired to think about global variables)

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
                WIDTH, HEIGHT = 16*board_width, 16*board_height
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            elif event.key == pygame.K_MINUS:
                if(board_width>1 and board_height>1):
                    board_width-=1
                    board_height-=1
                    WIDTH, HEIGHT = 16*board_width, 16*board_height
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            elif event.key == pygame.K_r:
                board_state = [[random.choice([0, 0, 0, 0, 0, 0, 0, 1]) for i in range(board_width)] for i in range(board_height)]

            elif event.key == pygame.K_RETURN:
                
                x, y = pygame.mouse.get_pos()
                i = x//16
                j = y//16
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
                rect = pygame.Rect(16*i, 16*j, 16, 16)
                pygame.draw.rect(surface=screen, rect=rect, color=primary)

    if(t%speed_ratio==0 and cant_think_of_a_good_variable_name_so_its_time_for_a_really_really_really_terrible_variable_name_because_its_really_long_hmm_im_really_bored_and_its_an_unusually_late_hour_of_the_night_so_i_feel_like_adding_more_to_this_really_really_really_really_really_really_really_really_really_long_variable_name_we_should_add_more_to_this_how_about_some_pi_3_1415926535897273238462643383279533846264338327950_idk_if_that_was_right_cuz_i_havent_checked_in_a_long_time_also_if_you_know_more_feel_free_to_submit_a_pull_request_first_you_fork_the_repository_then_make_edits_and_commits_and_then_click_the_contribute_or_create_a_pull_request_its_usually_a_big_big_green_red_button_very_clickable_so_you_just_click_that_and_click_submit_pull_request_then_if_its_right_i_might_accept_thanks_lol):
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
                
                if(board_state[i][j] and alive_neighbours not in [1, 2, 3, 4, 5]):
                    new_board[i][j] = 0
            
                if(not board_state[i][j] and alive_neighbours in {3}):
                    new_board[i][j] = 1

        board_state = new_board

                
    pygame.display.flip()
    clock.tick(120)

pygame.quit()