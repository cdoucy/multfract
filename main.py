from tkinter import *
from circle import circle
import numpy as np
import time
from sys import stderr

running = False

def init_window():
    win = Tk()

    win.title("multfract")
    win.geometry("1920x1080")
    win.protocol("WM_DELETE_WINDOW", close_win)
    return win

def init_canvas(win, circle_stat):
    canvas = Canvas(win, width=1920, height=1080, bg="white")

    canvas.pack()
    canvas.create_oval(circle_stat.x0, circle_stat.y0,
        circle_stat.x1, circle_stat.y1, outline="black")
    return canvas

def run_multfract(win, circle_stat, canvas, argv):
    global running
    n = int(argv[1])
    mod = int(argv[2])
    opt = int(argv[3])
    start = time.clock()
    lines = []
    tmp = 0
    status = True
    running = True

    while running:
        if status:
            points = get_points(circle_stat, mod)
            status = False
        if len(lines) >= mod:
            for i in range(len(lines) - mod + 1):
                canvas.delete(lines[i])
                del lines[i]
        lines.append(draw_lines(points, canvas, n, win, mod, tmp))
        tmp += 1
        if tmp == mod:
            if opt == 2:
                mod += 1
                n += 1
            else:
                if opt: mod += 1
                else: n += 1
            status = True
            tmp = 0
        win.update()

def main(argv):
    global circle
    win = init_window()
    circle_stat = circle()
    canvas = init_canvas(win, circle_stat)

    run_multfract(win, circle_stat, canvas, argv)
    win.destroy()

def get_points(circle_stat, mod):
    points = [[0 for i in range(2)] for k in range(mod)]

    for i in range(mod):
        points[i] = compute_coords(circle_stat, i, mod)
    return points

def compute_coords(circle_stat, i, mod):
    x = circle_stat.a + circle_stat.r * np.cos(2 * np.pi * i / mod)
    y = circle_stat.b + circle_stat.r * np.sin(2 * np.pi * i / mod)

    return x, y

def draw_lines(points, canvas, n, win, mod, i):
    k = (n * i) % mod
    line = canvas.create_line(points[i][0], points[i][1],
        points[k][0], points[k][1], fill = "black")

    canvas.pack()
    return line

def close_win():
    global running

    running = False