__author__ = 'TSK'


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        #左上のxy、右上のxy、円の色
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        #左右中央に円を移動
        self.canvas.move(self.id, 255, 110)
        self.x = 0
        self.y = -1
        #winfo_height()はキャンバスの高さを返している
        self.canvas_height = self.canvas.winfo_height()

    def move(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos [3] >= self.canvas_height:
            self.y = -1
