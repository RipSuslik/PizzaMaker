import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()
image = tk.PhotoImage(file="pizza.png")


def on_press(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def on_drag(event):
    global start_x, start_y
    dx, dy = event.x - start_x, event.y - start_y
    start_x, start_y = event.x, event.y  

canvas.bind("<ButtonPress-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)
start_x, start_y = 0, 0


def update():
    canvas.create_rectangle(0, 0, 800, 600, fill="white")
    canvas.create_rectangle(622, 360, 630, 148, fill="purple")
    canvas.create_rectangle(3200, 360, 600, 1408, fill="blue")
    canvas.create_rectangle(542, 366, 606, 148, fill="gray")
    canvas.create_rectangle(542, 366, 606, 148, fill="brown")
    canvas.create_oval(100,100,210,210, fill="green")
    canvas.create_image(start_x, start_y, anchor=tk.NW, image=image)
    root.after(16, update)  

root.after(16, update)

root.mainloop()

