import tkinter as tk
from tkinter import ttk
from organizer.core import FileOrganizer
from organizer.utils import (
    rules,
    history,
    set_folder,
    organize_action,
    undo_action,
    reset_action,
)


def run():
    root = tk.Tk()
    frame = ttk.Frame(root)
    frame.grid(column=0, row=0, sticky=("W, N ,E, S"))
    root.title("Auto_File_Organizer")

    txt_box = tk.Text(frame, height=13, width=40, wrap="word")
    txt_box.grid(column=1, row=1)

    SetFolder = ttk.Button(
        text="Set Folder",
        command=lambda: set_folder(txt_box, FileOrganizer, rules, history),
    )
    SetFolder.grid(column=1, row=2)

    Organize = ttk.Button(text="Organize", command=lambda: organize_action(txt_box))
    Organize.grid(column=2, row=3)

    Undo = ttk.Button(text="Undo", command=lambda: undo_action(txt_box))
    Undo.grid(column=2, row=2)

    Reset = ttk.Button(
        text="Reset",
        command=lambda: reset_action(txt_box),
    )
    Reset.grid(column=1, row=3)

    frame.mainloop()


run()
