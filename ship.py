import pygame as pg


class Ship:
    usage_info = None

    def __init__(self, size, image_path, is_horizontal):
        # size on board, in squares
        self.size = size
        # path to the image
        self.image_path = image_path
        # the image itself
        image_tmp = pg.image.load(image_path).convert_alpha()
        original_size = image_tmp.get_rect().size
        factor = 64 / 300
        new_size = (int(original_size[0] * factor), int(original_size[1] * factor))
        self.image = pg.transform.scale(image_tmp, new_size)
        self.rect = self.image.get_rect()
        self.horizontal = is_horizontal
        self.position_on_board = None

    def get_rect(self):
        """
        Get current position
        :return: current position, in pixels
        """
        return self.image.get_rect()

    def get_image(self):
        return self.image


class ShipUsageInfo:
    # Initialisation de la Font Module!
    pg.font.init()
    font = pg.font.Font("Always In My Heart.ttf", 25)

    def __init__(self, initial_count, text_coordinates):
        self.__count_unplaced = initial_count
        self.text = ShipUsageInfo.font.render(str(self.__count_unplaced), True, (0, 0, 0))
        self.text_coordinates = text_coordinates

    def get_count_unplaced(self):
        return self.__count_unplaced

    def decrement(self):
        self.__count_unplaced -= 1
        self.text = ShipUsageInfo.font.render(str(self.__count_unplaced), True, (0, 0, 0))

    def increment(self):
        self.__count_unplaced += 1
        self.text = ShipUsageInfo.font.render(str(self.__count_unplaced), True, (0, 0, 0))


class Carrier(Ship):
    usage_info = ShipUsageInfo(1, (932, 535))


class CarrierHorizontal(Carrier):
    def __init__(self, usage_info=None):
        super().__init__((5, 1), "./carrier_horizontal.png", True)

    @staticmethod
    def get_shelf_position():
        return 1037, 538


class CarrierVertical(Carrier):
    def __init__(self, usage_info=None):
        super().__init__((1, 5), "./carrier_vertical.png", False)

    @staticmethod
    def get_shelf_position():
        return 890, 143


class Cruiser(Ship):
    usage_info = ShipUsageInfo(2, (1004, 464))


class CruiserHorizontal(Cruiser):
    def __init__(self):
        super().__init__((4, 1), "./cruiser_horizontal_v5.png", True)

    @staticmethod
    def get_shelf_position():
        return 1101, 470


class CruiserVertical(Cruiser):
    def __init__(self):
        super().__init__((1, 4), "./cruiser_vertical_v6.png", False)

    @staticmethod
    def get_shelf_position():
        return 958, 143


class Destroyer(Ship):
    usage_info = ShipUsageInfo(3, (1069, 407))


class DestroyerHorizontal(Destroyer):
    def __init__(self):
        super().__init__((3, 1), "./destroyer_horizontal.png", True)

    @staticmethod
    def get_shelf_position():
        return 1165, 402


class DestroyerVertical(Destroyer):
    def __init__(self):
        super().__init__((1, 3), "./destroyer_vertical.png", False)

    @staticmethod
    def get_shelf_position():
        return 1026, 143


class Uboat(Ship):
    usage_info = ShipUsageInfo(4, (1141, 332))


class UboatHorizontal(Uboat):
    def __init__(self):
        super().__init__((2, 1), "./u-boat_horizontal.png", True)

    @staticmethod
    def get_shelf_position():
        return 1229, 334


class UboatVertical(Uboat):
    def __init__(self):
        super().__init__((1, 2), "./u-boat_vertical.png", False)

    @staticmethod
    def get_shelf_position():
        return 1094, 143
