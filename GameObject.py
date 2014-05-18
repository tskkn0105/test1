__author__ = 'TSK'

import Vector2D


class Ball:

    def __init__(self, canvas, color):
        self.canvas = canvas

        self.__size = 15
        self.__position = Vector2D.Vector2D(0.0, 0.0)
        self.__speed = Vector2D.Vector2D(0.0, 1.0)

        #左上のxy、右上のxy、円の色
        self.id = canvas.create_oval(0, 0, self.__size, self.__size, fill=color)
        #左右中央に円を移動
        self.canvas.move(self.id, 255, 110)

        #winfo_height()はキャンバスの高さを返している
        self.canvas_height = self.canvas.winfo_height()

    def Move(self):
        self.canvas.move(self.id, self.__speed.Get_x(), self.__speed.Get_y())
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.__speed.Set_y(1.0)
        if pos [3] >= self.canvas_height:
            self.__speed.Set_y(-1.0)
