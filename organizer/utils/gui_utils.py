import tkinter as tk
import json
from commands import args
from logger_code import get_logger

organizer_instance = {"obj": None}

if args.logfile:
    log = get_logger(log_to_file=True, log_file=args.logfile)
else:
    log = get_logger()


def set_folder(txt_box, FileOrganizer, rules, history):
    folder = txt_box.get("1.0", tk.END).strip()
    if folder:
        try:
            organizer_instance["obj"] = FileOrganizer(folder, rules, history, logger=log)  # type: ignore
            txt_box.delete(1.0, "end")
            txt_box.insert(tk.END, f"Folder set: {folder}")
            log.info(f"Folder set: {folder}")
        except Exception as e:
            organizer_instance["obj"] = None
            txt_box.delete(1.0, "end")
            txt_box.insert(tk.END, f"Please Enter Valid Path: {e}")
            log.warning(f"Please Enter Valid Path: {e}")
    else:
        txt_box.delete(1.0, "end")
        txt_box.insert(tk.END, "Please Enter Valid Path")


def organize_action(txt_box):
    org = organizer_instance["obj"]
    if org:
        try:
            org.organize()
            txt_box.delete(1.0, "end")
            txt_box.insert(tk.END, "Organized successfully.")
            log.info("Organized successfully.")
        except Exception as e:
            txt_box.delete(1.0, "end")
            txt_box.insert(tk.END, f"Error organizing folder: {e}")
            log.error(f"Error organizing folder: {e}")
    else:
        txt_box.delete(1.0, "end")
        txt_box.insert(tk.END, "Set folder first.")
        log.warning("Set folder first.")


def undo_action(txt_box):
    org = organizer_instance["obj"]
    if org:
        try:
            with open("undo.json", "r") as w:
                org.history = json.load(w)
            org.undo()
            txt_box.delete(1.0, "end")
            txt_box.insert(tk.END, "Undo successful.")
            log.info("Undo successful.")
        except Exception as e:
            txt_box.delete(1.0, "end")
            txt_box.insert(tk.END, f"Error undoing. {e}")
            log.error(f"Error undoing. {e}")
    else:
        txt_box.delete(1.0, "end")
        txt_box.insert(tk.END, "Set folder first.")
        log.warning("Set folder first.")


def reset_action(txt_box):
    org = organizer_instance["obj"]
    if org:
        try:
            org.reset()
            txt_box.delete(1.0, "end")
            txt_box.insert(tk.END, "Reset successful.")
            log.info("Reset successful.")
        except Exception as e:
            txt_box.delete(1.0, "end")
            txt_box.insert(tk.END, f"Error resetting: {e}")
            log.error(f"Error resetting: {e}")
    else:
        txt_box.delete(1.0, "end")
        txt_box.insert(tk.END, "Set folder first.")
        log.warning("Set folder first.")
