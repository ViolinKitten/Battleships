import pygame
from pygame.locals import *
import sys
from ship import *
from enum import Enum

PROGRAM_STATUS_SUCCESS = 0
PROGRAM_STATUS_ERROR = 1


class Mode(Enum):
    COORDINATE = 0
    PLACEMENT = 1
    BATTLE = 2


class GridCell(Enum):
    EMPTY = 0
    AROUND_SHIP = 1
    HEALTHY_SHIP = 2
    DESTROYED_SHIP = 3


class Application:
    GRID_CELL_SIZE = 64
    GRID_WIDTH = 10
    GRID_HEIGHT = 10

    def __init__(self):
        self.grid_columns = [182, 246, 311, 376, 440, 505, 569, 634, 698, 761]
        self.grid_rows = [79, 143, 207, 272, 336, 400, 464, 528, 592, 656]
        self.grid = []
        self.ships = set()
        for i_col in range(0, Application.GRID_WIDTH):
            grid_column = []
            for i_row in range(0, Application.GRID_HEIGHT):
                grid_column.append(GridCell.EMPTY)
            self.grid.append(grid_column)

    @staticmethod
    def find_cell_at_point(x, y):
        col = int((x - 181) / Application.GRID_CELL_SIZE)
        row = int((y - 78) / Application.GRID_CELL_SIZE)
        return col, row

    def determine_dropped_ship_location(self, initial_rectangle, ship_grid_size):
        """
        Determines the exact location of the ship (in pixels) when it is "dropped" on the grid
        :type ship_grid_size: tuple[int]
        :param ship_grid_size: ship grid size
        :type initial_rectangle: pygame.Rect
        :param initial_rectangle: the rectangle spanning by the ship about to be dropped
        :return: TBD
        """
        first_cell_center_x = initial_rectangle.x + initial_rectangle.width / (2 * ship_grid_size[0])
        first_cell_center_y = initial_rectangle.y + initial_rectangle.height / (2 * ship_grid_size[1])
        col, row = self.find_cell_at_point(first_cell_center_x, first_cell_center_y)

        return col, row

    def can_drop_ship(self, first_grid_cell, ship):
        """
        :type first_grid_cell: tuple
        :param first_grid_cell: coordinate of the top left grid cell where the ship is trying to be placed
        :type ship: Ship
        :param ship:
        :return:
        """
        if ship.__class__.usage_info.get_count_unplaced() == 0:
            return False
        if first_grid_cell[0] + ship.size[0] > Application.GRID_WIDTH or first_grid_cell[0] < 0:
            return False
        if first_grid_cell[1] + ship.size[1] > Application.GRID_HEIGHT or first_grid_cell[1] < 0:
            return False
        for i_col in range(first_grid_cell[0]-1, first_grid_cell[0] + ship.size[0]+1):
            for i_row in range(first_grid_cell[1]-1, first_grid_cell[1] + ship.size[1]+1):
                if not self.grid[i_col][i_row] == GridCell.EMPTY:
                    return False

        return True

    def drop_ship(self, first_grid_cell, ship):
        """
        :type first_grid_cell: tuple[int]
        :param first_grid_cell:
        :type ship: Ship
        :param ship:
        :return:
        """

        x = self.grid_columns[first_grid_cell[0]]
        y = self.grid_rows[first_grid_cell[1]]
        ship.rect = ship.rect.move(x - ship.rect.x, y - ship.rect.y)
        self.ships.add(ship)
        ship.position_on_board = first_grid_cell
        ship.__class__.usage_info.decrement()

        for col in range(first_grid_cell[0], first_grid_cell[0] + ship.size[0]):
            for row in range(first_grid_cell[1], first_grid_cell[1] + ship.size[1]):
                self.grid[col][row] = GridCell.HEALTHY_SHIP
                if col > 0:
                    if self.grid[col - 1][row] == GridCell.EMPTY:
                        self.grid[col - 1][row] = GridCell.AROUND_SHIP
                    if row > 0 and self.grid[col - 1][row - 1] == GridCell.EMPTY:
                        self.grid[col - 1][row - 1] = GridCell.AROUND_SHIP
                    if row < Application.GRID_HEIGHT - 1 and self.grid[col - 1][row + 1] == GridCell.EMPTY:
                        self.grid[col - 1][row + 1] = GridCell.AROUND_SHIP

                if col < Application.GRID_WIDTH - 1:
                    if self.grid[col + 1][row] == GridCell.EMPTY:
                        self.grid[col + 1][row] = GridCell.AROUND_SHIP
                    if row > 0 and self.grid[col + 1][row - 1] == GridCell.EMPTY:
                        self.grid[col + 1][row - 1] = GridCell.AROUND_SHIP
                    if row < Application.GRID_HEIGHT - 1 and self.grid[col + 1][row + 1] == GridCell.EMPTY:
                        self.grid[col + 1][row + 1] = GridCell.AROUND_SHIP

                if row > 0 and self.grid[col][row - 1] == GridCell.EMPTY:
                    self.grid[col][row - 1] = GridCell.AROUND_SHIP
                if row < Application.GRID_HEIGHT - 1 and self.grid[col][row + 1] == GridCell.EMPTY:
                    self.grid[col][row + 1] = GridCell.AROUND_SHIP

    def remove_ship(self, ship):
        self.ships.remove(ship)
        ship.__class__.usage_info.increment()
        first_grid_cell = ship.position_on_board
        for col in range(first_grid_cell[0], first_grid_cell[0] + ship.size[0]):
            for row in range(first_grid_cell[1], first_grid_cell[1] + ship.size[1]):
                self.grid[col][row] = GridCell.EMPTY
                if col > 0:
                    if self.grid[col - 1][row] == GridCell.EMPTY:
                        self.grid[col - 1][row] = GridCell.AROUND_SHIP
                    if row > 0 and self.grid[col - 1][row - 1] == GridCell.EMPTY:
                        self.grid[col - 1][row - 1] = GridCell.AROUND_SHIP
                    if row < Application.GRID_HEIGHT - 1 and self.grid[col - 1][row + 1] == GridCell.EMPTY:
                        self.grid[col - 1][row + 1] = GridCell.AROUND_SHIP

                if col < Application.GRID_WIDTH - 1:
                    if self.grid[col + 1][row] == GridCell.EMPTY:
                        self.grid[col + 1][row] = GridCell.AROUND_SHIP
                    if row > 0 and self.grid[col + 1][row - 1] == GridCell.EMPTY:
                        self.grid[col + 1][row - 1] = GridCell.AROUND_SHIP
                    if row < Application.GRID_HEIGHT - 1 and self.grid[col + 1][row + 1] == GridCell.EMPTY:
                        self.grid[col + 1][row + 1] = GridCell.AROUND_SHIP

                if row > 0 and self.grid[col][row - 1] == GridCell.EMPTY:
                    self.grid[col][row - 1] = GridCell.AROUND_SHIP
                if row < Application.GRID_HEIGHT - 1 and self.grid[col][row + 1] == GridCell.EMPTY:
                    self.grid[col][row + 1] = GridCell.AROUND_SHIP

    def main(self):
        # Initialisation de la bibliothèque Pygame
        pygame.init()

        # Ouverture de la fenêtre Pygame
        larg_fenetre = 1419
        haut_fenetre = 731
        main_window = pygame.display.set_mode((larg_fenetre, haut_fenetre))

        # Chargement et collage du background
        background = pygame.image.load("bataille1.png").convert()

        # Chargement et collage du ships
        shelf_carrier_vertical = CarrierVertical()
        shelf_crusier_vertical = CruiserVertical()
        shelf_destroyer_vertical = DestroyerVertical()
        shelf_uboat_vertical = UboatVertical()

        shelf_carrier_horizontal = CarrierHorizontal()
        shelf_crusier_horizontal = CruiserHorizontal()
        shelf_destroyer_horizontal = DestroyerHorizontal()
        shelf_uboat_horizontal = UboatHorizontal()

        ship_classes = [Carrier, Cruiser, Destroyer, Uboat]

        shelf_ships = [shelf_carrier_vertical, shelf_crusier_vertical, shelf_destroyer_vertical, shelf_uboat_vertical,
                       shelf_carrier_horizontal, shelf_crusier_horizontal, shelf_destroyer_horizontal,
                       shelf_uboat_horizontal]

        for i_shelf_ship in range(0, len(shelf_ships)):
            shelf_ship = shelf_ships[i_shelf_ship]
            shelf_ship.rect = shelf_ship.rect.move(shelf_ship.get_shelf_position())
            main_window.blit(shelf_ship.get_image(), shelf_ship.rect)

        # Rafraîchissement de l'écran
        pygame.display.flip()

        continue_game = True
        mouse_up = True
        mode = Mode.PLACEMENT
        ship_chosen_for_placement = None

        # Main program loop
        while continue_game:
            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:  # Si on clique sur le bouton quitter
                    continue_game = False  # la boucle s'arrête
                if event.type == KEYDOWN:  # Si on appuye sur une touche du clavier
                    if event.key == K_ESCAPE:  # Si cette touche est la touche echap
                        continue_game = False  # On arrête la boucle
                    elif event.key == K_p:
                        mode = Mode.PLACEMENT
                    elif event.key == K_c:
                        mode = Mode.COORDINATE

            main_window.blit(background, (0, 0))
            for ship_class in ship_classes:
                main_window.blit(ship_class.usage_info.text, ship_class.usage_info.text_coordinates)

            if mode == Mode.COORDINATE:
                for i_shelf_ship in range(0, len(shelf_ships)):
                    shelf_ship = shelf_ships[i_shelf_ship]
                    main_window.blit(shelf_ship.get_image(), shelf_ship.rect)
                if event.type == MOUSEBUTTONDOWN and mouse_up:
                    (x, y) = event.pos
                    print(x, ", ", y)
                    mouse_up = False
                elif event.type == MOUSEBUTTONUP:
                    mouse_up = True
            elif mode == Mode.PLACEMENT:
                # draw shelf
                for shelf_ship in shelf_ships:
                    main_window.blit(shelf_ship.get_image(), shelf_ship.rect)
                    # a shelf ship has been clicked
                    if event.type == MOUSEBUTTONDOWN and \
                            shelf_ship.rect.collidepoint(event.pos) and ship_chosen_for_placement is None:
                        ShipClass = shelf_ship.__class__
                        print("Making ship: ", ShipClass.__name__)
                        ship_chosen_for_placement = ShipClass()

                ship_picked_up = False
                for ship in self.ships:
                    main_window.blit(ship.get_image(), ship.rect)
                    # a non-shelf ship has been clicked
                    if event.type == MOUSEBUTTONDOWN and \
                            ship.rect.collidepoint(event.pos) and ship_chosen_for_placement is None:
                        ship_chosen_for_placement = ship
                        ship_picked_up = True
                if ship_picked_up:
                    self.remove_ship(ship_chosen_for_placement)

                if ship_chosen_for_placement is not None: # a ship is being dragged
                    ship_chosen_for_placement.rect.center = event.pos
                    main_window.blit(ship_chosen_for_placement.get_image(), ship_chosen_for_placement.rect)
                if event.type == MOUSEBUTTONDOWN and mouse_up:
                    mouse_up = False
                elif event.type == MOUSEBUTTONUP:
                    mouse_up = True
                    if ship_chosen_for_placement is not None: # ship is being dropped
                        coords = self.determine_dropped_ship_location(ship_chosen_for_placement.rect,
                                                                      ship_chosen_for_placement.size)
                        print("Placing ship at ", coords)
                        if self.can_drop_ship(coords, ship_chosen_for_placement):
                            self.drop_ship(coords, ship_chosen_for_placement)
                        ship_chosen_for_placement = None

            pygame.display.flip()

        pygame.quit()
        return PROGRAM_STATUS_SUCCESS


if __name__ == "__main__":
    app = Application()
    sys.exit(app.main())
