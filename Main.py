__author__ = 'TSK'

import tkinter
import time

import GameObject


tk = tkinter.Tk()
#タイトルをつける
tk.title("Game")
#(0,0)で縦方向、横方向にウィンドウサイズを変更できなくさせる
tk.resizable(0,0)
#全てのウィンドウより上に配置
tk.wm_attributes("-topmost",1)
#bd=0とhighlightthickness=0でキャンバスの外側の線を無くす
canvas = tkinter.Canvas(tk,width=500, height=400, bd=0, highlightthickness=0)
#キャンバスを表示
canvas.pack()
#tkinterを初期化
tk.update()

#ボールオブジェクトを作成
ball = GameObject.Ball(canvas, "red")

#メインループ
while True:
    ball.move()

    #画面書き換え処理とか
    #############################
    tk.update_idletasks()
    tk.update()
    #待機時間second
    time.sleep(0.016)
    #############################