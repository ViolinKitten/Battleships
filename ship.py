import pygame as pg


class Ship:
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

    def get_rect(self):
        """
        Get current position
        :return: current position, in pixels
        """
        return self.image.get_rect()

    def get_image(self):
        return self.image


class CarrierHorizontal(Ship):
    def __init__(self):
        super().__init__((5, 1), "./carrier_horizontal.png", True)


class CarrierVertical(Ship):
    def __init__(self):
        super().__init__((1, 5), "./carrier_vertical.png", False)


class CruiserHorizontal(Ship):
    def __init__(self):
        super().__init__((4, 1), "./cruiser_horizontal_v5.png", True)


class CruiserVertical(Ship):
    def __init__(self):
        super().__init__((1, 4), "./cruiser_vertical_v6.png", False)


class DestroyerHorizontal(Ship):
    def __init__(self):
        super().__init__((3, 1), "./destroyer_horizontal.png", True)


class DestroyerVertical(Ship):
    def __init__(self):
        super().__init__((1, 3), "./destroyer_vertical.png", False)


class UboatHorizontal(Ship):
    def __init__(self):
        super().__init__((2, 1), "./u-boat_horizontal.png", True)


class UboatVertical(Ship):
    def __init__(self):
        super().__init__((1, 2), "./u-boat_vertical.png", False)
