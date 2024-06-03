import pygame
import random
import math


class Particle:
    def __init__(self, fall_speed, liquid, sandiness, gravity, colour, thickness):
        self.fall_speed = fall_speed
        self.liquid = liquid
        self.sandiness = sandiness
        self.gravity = gravity
        self.colour = colour
        self.thickness = thickness


def initiate_a_playing_field(x, y, with_what):
    playing_board = [[with_what for _ in range(x)] for _ in range(y)]
    return playing_board


def drawing_the_grid(x, y, size, where):
    for i in range(x - 1):
        pygame.draw.line(where, (35, 35, 35), ((i + 1) * size, 0), ((i + 1) * size, y * size))
    for i in range(y):
        pygame.draw.line(where, (35, 35, 35), (0, (i + 1) * size), (x * size, (i + 1) * size))


def drawing_the_particles(x, y, size, where, particles, board):
    which_row = 0
    global max_x
    while which_row < y:
        which_column = 0
        if board[which_row].count(0) < max_x:
            while which_column < x:
                if board[which_row][which_column] != 0:
                    # randomium.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    pygame.draw.rect(where, particles[board[which_row][which_column]].colour,
                                     (which_column * size, which_row * size, size, size))
                which_column += 1
        which_row += 1


def calc_position(size, max_x_in_fun):
    global previous, height
    x, y = pygame.mouse.get_pos()
    x = math.floor(x / size)
    y = math.floor(y / size)
    if max_x_in_fun > x >= 0 and int(height * 1.1) // size > y >= 0:
        previous = [x, y]
        return x, y
    else:
        return previous


def draw_menu(selected, width_fun, height_fun, screen):
    i = 0
    for i in range(11):
        pygame.draw.rect(screen, (255, 255, 255),
                         ((width_fun / 10) * i + width_fun / 45, height_fun + height_fun / 47, height_fun / 13,
                          height_fun / 13,))
        if i != selected:
            pygame.draw.rect(screen, (0, 0, 0), (
                (width_fun / 10) * i + width_fun / 45 + height_fun / 450,
                height_fun + height_fun / 47 + height_fun / 450, height_fun / 14,
                height_fun / 14,))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (
                (width_fun / 10) * i + width_fun / 45 + height_fun / 220,
                height_fun + height_fun / 47 + height_fun / 220, height_fun / 15,
                height_fun / 15,))
    pygame.draw.rect(screen, (0, 0, 0), (
        (width_fun / 10) * i + width_fun / 45 + height_fun / 450, height_fun + height_fun / 47 + height_fun / 450,
        height_fun / 14, height_fun / 14,))


def inside_boundary(check_x, check_y):
    global max_x, max_y
    if max_x > check_x >= 0 and max_y > check_y >= 0:
        return True
    return False


def draw_mouse(screen_in_fun, mouse_x_in_fun, mouse_y_in_fun, brushes_in_fun, brush_size, what_to_draw, list_particles,
               sizer, max_y_in_fun):
    color = list_particles[what_to_draw + 1].colour
    color = [i * 0.7 for i in color]
    if mouse_y_in_fun < max_y_in_fun:
        if brush_size == 0:
            pygame.draw.rect(screen_in_fun, color, (mouse_x_in_fun * sizer, mouse_y_in_fun * sizer, sizer, sizer))

        else:
            for loc_x, idk_something_im_bad_at_naming_things in enumerate(brushes_in_fun[brush_size - 1]):
                loc_x -= brush_size
                for loc_y, value in enumerate(idk_something_im_bad_at_naming_things):
                    loc_y -= brush_size
                    if value == 1:
                        if inside_boundary(loc_x + mouse_x_in_fun, loc_y + mouse_y_in_fun):
                            pygame.draw.rect(screen_in_fun, color, (
                                (mouse_x_in_fun + loc_x) * sizer, (mouse_y_in_fun + loc_y) * sizer, sizer, sizer))


def buttons(what_to_be_added):
    how_long_button_show = 50
    global drawing_size
    global main_board
    global what_was_added
    global max_x, max_y, width, height, screen
    if what_to_be_added == 9:
        main_board = initiate_a_playing_field(max_x, max_y, 0)
        draw_menu(what_to_be_added, width, height, screen)
        pygame.display.flip()
        pygame.time.wait(how_long_button_show)
        return what_was_added

    if what_to_be_added == 8:  # make the drawing bigger
        if drawing_size < 3:
            drawing_size += 1
        draw_menu(what_to_be_added, width, height, screen)
        pygame.display.flip()
        pygame.time.wait(how_long_button_show)
        return what_was_added

    if what_to_be_added == 7:  # make the drawing smaller
        if drawing_size > 0:
            drawing_size -= 1
        draw_menu(what_to_be_added, width, height, screen)
        pygame.display.flip()
        pygame.time.wait(how_long_button_show)
        return what_was_added
    return what_to_be_added


def drawing_stuff_by_adding_them_to_a_list(max_y_fun, mouse_y_fun, mouse_x_fun, selected_menu_slot_fun,
                                           brushes_in_fun, brush_size, rez):
    global what_was_added, selected_menu_slot, height, width
    if mouse_y_fun < max_y_fun and pygame.mouse.get_pressed()[0]:
        if brush_size == 0:
            main_board[mouse_y_fun][mouse_x_fun] = selected_menu_slot_fun + 1
        else:
            for loc_x, idk_something_im_bad_at_naming_things in enumerate(brushes_in_fun[brush_size - 1]):
                loc_x -= brush_size
                for loc_y, value in enumerate(idk_something_im_bad_at_naming_things):
                    loc_y -= brush_size
                    if value == 1:
                        if inside_boundary(loc_x + mouse_x_fun, loc_y + mouse_y_fun):
                            main_board[mouse_y_fun + loc_y][mouse_x_fun + loc_x] = selected_menu_slot_fun + 1
    elif (max_y_fun * 1.1) > mouse_y_fun > max_y_fun and pygame.mouse.get_pressed()[0]:
        cos1 = (width / 10) / rez
        a = int(mouse_x_fun // cos1)
        if a > 6:
            what_was_added = selected_menu_slot_fun
        selected_menu_slot = a
    elif mouse_y_fun < max_y_fun and pygame.mouse.get_pressed()[2]:
        if brush_size == 0:
            main_board[mouse_y_fun][mouse_x_fun] = 0
        else:
            for loc_x, idk_something_im_bad_at_naming_things in enumerate(brushes_in_fun[brush_size - 1]):
                loc_x -= brush_size
                for loc_y, value in enumerate(idk_something_im_bad_at_naming_things):
                    loc_y -= brush_size
                    if value == 1:
                        if inside_boundary(loc_x + mouse_x_fun, loc_y + mouse_y_fun):
                            main_board[mouse_y_fun + loc_y][mouse_x_fun + loc_x] = 0


def scaning_for_where_fluids_can_go(board, maxi_x, maxi_y, particles):
    current_y = -1
    to_be_returned = []
    while current_y < maxi_y - 1:
        current_y += 1
        current_x = 0
        in_this_line = []
        how_much_water_in_this_part = 0
        start_of_current_x = 0
        how_much_air = 0
        while current_x < maxi_x:
            current_particle = board[current_y][current_x]
            part = particles[current_particle]
            if part.liquid:
                how_much_water_in_this_part += 1
            elif current_particle == 0:
                how_much_air += 1
            if not (part.liquid or current_particle == 0) and current_x != start_of_current_x and (
                    how_much_air != 0 or how_much_water_in_this_part != 0):
                if how_much_water_in_this_part != current_x - start_of_current_x:
                    in_this_line.append([start_of_current_x, current_x, how_much_water_in_this_part])
                start_of_current_x = current_x + 1
                how_much_air = 0
                how_much_water_in_this_part = 0
            elif how_much_water_in_this_part == 0 and how_much_air == 0:
                start_of_current_x = current_x + 1
            current_x += 1
        if current_x != start_of_current_x and (how_much_water_in_this_part != 0 or how_much_air != 0):
            if how_much_water_in_this_part != current_x - start_of_current_x:
                in_this_line.append([start_of_current_x, current_x, how_much_water_in_this_part])

        to_be_returned.append(in_this_line.copy())
    return to_be_returned


def physics_simulation(board, particles, max_x, max_y, water_free_places):
    current_y = max_y - 1

    while current_y >= 0:
        current_x = 0
        if board[current_y].count(0) < max_x:
            while current_x < max_x:
                current_particle_value = board[current_y][current_x]
                if current_particle_value != 0:
                    if inside_boundary(current_x, current_y + 1):
                        under = board[current_y + 1][current_x]
                    else:
                        under = None
                    part = particles[current_particle_value]
                    will_it_fall = random.randint(0, 100)
                    if under == 0 and part.gravity:
                        if part.fall_speed >= will_it_fall:
                            board[current_y + 1][current_x] = current_particle_value
                            board[current_y][current_x] = 0

                    elif under is not None and particles[board[current_y][current_x]].thickness > particles[board[current_y + 1][current_x]].thickness and random.randint(0, 100) < particles[board[current_y][current_x]].thickness - particles[board[current_y + 1][current_x]].thickness and (particles[board[current_y + 1][current_x]].liquid or particles[board[current_y][current_x]].liquid) and particles[board[current_y][current_x]].thickness <= 100:
                        board[current_y][current_x] = board[current_y + 1][current_x]
                        board[current_y + 1][current_x] = current_particle_value

                    elif under is not None and part.liquid:
                        if water_free_places[current_y + 1]:

                            for current_index_water, places in enumerate(water_free_places[current_y + 1]):
                                if water_free_places[current_y + 1][current_index_water][2] != \
                                        water_free_places[current_y + 1][current_index_water][1]:
                                    left_point = places[0]
                                    right_point = places[1]
                                    if left_point - 1 <= current_x <= right_point:

                                        left_x = right_x = current_x
                                        left_x -= 1
                                        right_x += 1
                                        how_right = how_left = 0
                                        right = True
                                        left = True
                                        while True:

                                            if right_x <= right_point and right:
                                                if inside_boundary(right_x, current_y + 1):
                                                    if board[current_y + 1][right_x] != 0:
                                                        right_x += 1
                                                        how_right += 1
                                                        if not inside_boundary(right_x, current_y):
                                                            right = False
                                                            how_right = -1
                                                    elif right:
                                                        right = False
                                                else:
                                                    right = False
                                                    how_right = -1
                                            elif right:
                                                how_right = -1
                                                right = False
                                            if left_x >= left_point and left:
                                                if inside_boundary(left_x, current_y + 1):
                                                    if board[current_y + 1][left_x] != 0:
                                                        left_x -= 1
                                                        how_left += 1
                                                        if not inside_boundary(left_x, current_y):
                                                            left = False
                                                            how_left = -1
                                                    else:
                                                        left = False
                                                else:
                                                    left = False
                                                    how_left = -1
                                            elif left:
                                                how_left = -1
                                                left = False
                                            if right is False and left is False:
                                                break

                                        if how_left == how_right and how_left != -1:
                                            hym = [left_x, right_x]
                                            board[current_y + 1][random.choice(hym)] = current_particle_value
                                            board[current_y][current_x] = 0
                                            water_free_places[current_y + 1][current_index_water][2] += 1
                                            break
                                        elif how_left > how_right:
                                            if how_right != -1:
                                                board[current_y + 1][right_x] = current_particle_value
                                                board[current_y][current_x] = 0
                                                water_free_places[current_y + 1][current_index_water][2] += 1
                                                break
                                            else:
                                                board[current_y + 1][left_x] = current_particle_value
                                                board[current_y][current_x] = 0
                                                water_free_places[current_y + 1][current_index_water][2] += 1
                                                break
                                        elif how_right > how_left:
                                            if how_left != -1:
                                                board[current_y + 1][left_x] = current_particle_value
                                                board[current_y][current_x] = 0
                                                water_free_places[current_y + 1][current_index_water][2] += 1
                                                break
                                            else:
                                                board[current_y + 1][right_x] = current_particle_value
                                                board[current_y][current_x] = 0
                                                water_free_places[current_y + 1][current_index_water][2] += 1
                                                break

                    elif under is not None and part.sandiness > 0:
                        where = []
                        if inside_boundary(current_x - 1, current_y + 1):
                            if board[current_y + 1][current_x - 1] == 0 or (particles[board[current_y + 1][current_x - 1]].liquid and particles[board[current_y][current_x]].thickness > particles[board[current_y + 1][current_x - 1]].thickness):
                                where.append(-1)
                        if inside_boundary(current_x + 1, current_y + 1):
                            if board[current_y + 1][current_x + 1] == 0 or (particles[board[current_y + 1][current_x + 1]].liquid and particles[board[current_y][current_x]].thickness > particles[board[current_y + 1][current_x + 1]].thickness):
                                where.append(1)
                        if len(where) == 2:
                            board[current_y][current_x] = board[current_y + 1][current_x + random.choice(where)]
                            board[current_y + 1][current_x + random.choice(where)] = current_particle_value
                        elif len(where) == 1:
                            check_sandiness = random.randint(0, 100) < part.sandiness
                            if check_sandiness:
                                board[current_y][current_x] = board[current_y + 1][current_x + where[0]]
                                board[current_y + 1][current_x + where[0]] = current_particle_value

                current_x += 1
            current_y -= 1

        else:
            current_y -= 1


def melting_ice(board, max_x_fun, max_y_fun):
    current_y = max_y_fun - 1

    while current_y >= 0:
        current_x = 0
        if board[current_y].count(0) < max_x_fun:
            while current_x < max_x_fun:
                chance = 0
                if board[current_y][current_x] == 2:
                    if inside_boundary(current_x, current_y + 1):
                        if board[current_y + 1][current_x] == 5:
                            chance += 1
                    if inside_boundary(current_x + 1, current_y):
                        if board[current_y][current_x + 1] == 5:
                            chance += 1
                    if inside_boundary(current_x, current_y - 1):
                        if board[current_y - 1][current_x] == 5:
                            chance += 1
                    if inside_boundary(current_x - 1, current_y):
                        if board[current_y][current_x - 1] == 5:
                            chance += 1
                    if random.randint(0,100) < chance:
                        board[current_y][current_x] = 5
                current_x += 1
        current_y -= 1


if __name__ == '__main__':

    brushes = [[[0, 1, 0], [1, 1, 1], [0, 1, 0]],
               [[0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0]],
               [[0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0]]]
    drawing_size = 0
    what_was_added = 0
    selected_menu_slot = 0
    previous = [0, 0]
    nothing = Particle(0, False, 0, False, (0, 0, 0), 0)
    sand = Particle(100, False, 30, True, (214, 178, 128), 35)
    water = Particle(100, True, 0, True, (0, 40, 124), 10)
    leaf = Particle(15, False, 5, True, (0, 240, 24), 5)
    stone = Particle(0, False, 0, False, (100, 100, 100), 1000)
    ice = Particle(0, False, 0, False, (100, 140, 255), 1000)
    lava = Particle(40, True, 0, True, (200, 40, 40), 30)
    all_particles = [nothing, sand, water, leaf, stone, ice, lava]
    clock = pygame.time.Clock()
    width, height = 1420, 880
    mouse_x, mouse_y = 0, 0
    pixel_size = 20
    pygame.init()
    screen = pygame.display.set_mode((width, height * 1.1))
    running = True
    max_x = width // pixel_size
    max_y = height // pixel_size
    main_board = initiate_a_playing_field(max_x, max_y, 2)
    temperature_board = initiate_a_playing_field(max_x, max_y, 25)
    while running:

        pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))
        mouse_x, mouse_y = calc_position(pixel_size, max_x)
        water_can_go_here = scaning_for_where_fluids_can_go(main_board, max_x,
                                                            max_y, all_particles)
        physics_simulation(main_board, all_particles, max_x, max_y, water_can_go_here)
        melting_ice(main_board, max_x, max_y)
        drawing_the_particles(max_x, max_y, pixel_size, screen, all_particles, main_board)
        draw_mouse(screen, mouse_x, mouse_y, brushes, drawing_size, selected_menu_slot, all_particles, pixel_size,
                   max_y)
        drawing_the_grid(max_x, max_y, pixel_size, screen)
        draw_menu(selected_menu_slot, width, height, screen)
        drawing_stuff_by_adding_them_to_a_list(max_y, mouse_y, mouse_x, selected_menu_slot, brushes, drawing_size,
                                               pixel_size)
        # print(water_can_go_here)
        selected_menu_slot = buttons(selected_menu_slot)
        # print(main_board)
        pygame.display.flip()
        """
        game_speed = 0
        game_speed = 1000//pixel_size
        game_speed = 5
        """
        clock.tick(60)
        # print(clock.get_fps())
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
