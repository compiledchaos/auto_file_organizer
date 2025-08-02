import tkinter as tk
from tkinter import ttk
from organizer.core import FileOrganizer
from organizer.utils import (
    rules_func,
    history,
    set_folder,
    organize_action,
    undo_action,
    reset_action,
)
from organizer.logger_code import get_logger

log = get_logger()


def run_gui(args):
    """
    Runs the graphical user interface for file organization.

    Creates a window with four buttons and a text box:
    - Set Folder: Set the folder to be organized.
    - Organize: Organize the files in the folder according to the rules.
    - Undo: Undo the last organization action.
    - Reset: Reset the history of organization actions.

    The text box is used to display messages about the actions taken.

    Args:
        args: Parsed command line arguments.

    Returns:
        None
    """
    root = tk.Tk()
    frame = ttk.Frame(root)
    frame.grid(column=0, row=0, sticky=("W, N ,E, S"))
    root.title("Auto_File_Organizer")

    history_data = history(args.history)
    rules = rules_func()
    txt_box = tk.Text(frame, height=13, width=40, wrap="word")
    txt_box.grid(column=1, row=1)
    SetFolder = ttk.Button(
        text="Set Folder",
        command=lambda: set_folder(txt_box, FileOrganizer, rules, history_data, args),
    )
    SetFolder.grid(column=1, row=2)

    Organize = ttk.Button(
        text="Organize", command=lambda: organize_action(txt_box, args)
    )
    Organize.grid(column=2, row=3)

    Undo = ttk.Button(text="Undo", command=lambda: undo_action(txt_box, args))
    Undo.grid(column=2, row=2)

    Reset = ttk.Button(
        text="Reset",
        command=lambda: reset_action(txt_box, args),
    )
    Reset.grid(column=1, row=3)
    frame.mainloop()
