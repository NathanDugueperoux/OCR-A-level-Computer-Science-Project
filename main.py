import tkinter as tk
import telemetrix_uno_r4

window = tk.Tk()
window.geometry("1000x500")
text = tk.Label(window, text="Controls")
frame = tk.Frame(window, width=1000, height=1000, bg="red", highlightbackground="black", highlightthickness=1 )
frame.pack(pady=100, padx=100)


def track_motion(event):
    x = event.x
    y = event.y
    print(f"({x}, {y})")


def move_robot(event):
    if event.char == "e":
        print("go up")
    if event.char == "q":
        print("go down")


frame.bind("<Motion>", track_motion)
window.bind("<Key>", move_robot)

window.mainloop()
