


import tkinter as tk
from tkinter import messagebox
import mouse
import keyboard

running = False
delay = 0

def start_clicker():
    """Запускає процес автоклікання, отримує швидкість з поля вводу."""
    global running, delay

    try:
        clicks_per_second = int(entry.get())

        if clicks_per_second <= 0:
            messagebox.showerror("Помилка", "Швидкість має бути більше 0!")
            return
        
        delay = int(1000 / clicks_per_second)

        messagebox.showinfo("Auto Clicker", "Auto Clicker розпочато! Натисніть 'ESC', щоб зупинити.")
        running = True
        scedule_click()

    except ValueError:
        messagebox.showerror("Помилка вводу", "Будь ласка, введіть коректне число кліків на секунду.")

def scedule_click():
    """Виконує один клік планує наступний, якщо клікер активний."""
    if running:
        mouse.click()

        root.after(delay, scedule_click)

def exit_app():
    """"Зупиняє клікер та закриває вікно програми."""
    global running

    if running:
        running = False

    messagebox.showinfo("Auto Clicker", "Auto Clicker 3ynnHeHo.")
    root.destroy()

def show_info(event):
    """Відображає інформаційне повідомлення (прив'язано до клавіші 'i')."""
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x220")
root.resizable(False, False)
root.configure(bg="#e0f7fa")

root.bind('i', show_info)

title_label = tk.Label(
    root,
    text="Auto Clicker",
    font=("Trebuchet MS", 16, "bold"),
    bg="#e0f7fa",
    fg="#00796b"
)
title_label.pack(pady=10)

label = tk.Label(
    root,
    text="Кліків на секунду:",
    font=("Trebuchet MS", 12),
    bg="#e0f7fa",
    fg="#00796b"
)
label.pack(pady=5)

entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=10,
    justify='center'
)
entry.pack(pady=15)
entry.insert(0, "10")

button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(10, 30))

start_button = tk.Button(
    button_frame,
    text="Почати",
    command=start_clicker,
    bg="#4caf50",
    activebackground="#66bb6a",
    fg="white",
    font=("Trebuchet MS", 12),
    width=8
)
start_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(
    button_frame,
    text="Вийти",
    command=exit_app,
    bg="#f44336",
    activebackground="#ef5350",
    fg="white",
    font=("Trebuchet MS", 12),
    width=8
)
exit_button.grid(row=0, column=1, padx=10)

keyboard.add_hotkey('esc', exit_app)

root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()