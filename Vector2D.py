__author__ = 'TSK'


class Vector2D:

    def __init__(self, x_float=0.0, y_float=0.0):
        self.__x = x_float
        self.__y = y_float

    def Get_x(self):
        return self.__x

    def Get_y(self):
        return self.__y

    def Set_x(self, x_float):
        self.__x = x_float

    def Set_y(self, y_float):
        self.__y = y_float