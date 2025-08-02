import tkinter as tk
import json
from organizer.utils.logger_setup import setup

organizer_instance = {"obj": None}


def set_folder(txt_box, FileOrganizer, rules, history, args):
    """
    Sets the folder to be organized.

    Args:
        txt_box: The text box widget used to display messages.
        FileOrganizer: The FileOrganizer class used to organize files.
        rules: The rules for organizing files.
        history: The history of file moves.
        args: Parsed command line arguments.

    The function sets the folder to be organized by creating a new FileOrganizer instance
    with the specified folder, rules, history, and logger. If the folder is valid, the
    function updates the organizer_instance dictionary with the new FileOrganizer instance.
    If the folder is invalid, the function displays an error message in the text box.
    """
    log = setup(args)

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


def organize_action(txt_box, args):
    """
    Organizes the set folder according to the rules specified.

    The function attempts to organize the set folder using the FileOrganizer instance
    stored in the organizer_instance dictionary. If the folder has been set and the
    organization is successful, the function displays a success message in the text
    box and logs the event. If the folder has not been set or an error occurs during
    organization, the function displays an appropriate error message in the text box
    and logs the event.

    Args:
        txt_box: The text box widget used to display messages.
        args: Parsed command line arguments.

    Returns:
        None
    """
    log = setup(args)

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


def undo_action(txt_box, args):
    """
    Undoes the last organization action.

    The function attempts to undo the last organization action using the FileOrganizer
    instance stored in the organizer_instance dictionary. If the undo is successful,
    the function displays a success message in the text box and logs the event. If the
    undo is not successful or an error occurs, the function displays an appropriate
    error message in the text box and logs the event.

    Args:
        txt_box: The text box widget used to display messages.
        args: Parsed command line arguments.

    Returns:
        None
    """
    log = setup(args)

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


def reset_action(txt_box, args):
    """
    Resets the history of organization actions.

    The function attempts to reset the history of organization actions using the
    FileOrganizer instance stored in the organizer_instance dictionary. If the reset
    is successful, the function displays a success message in the text box and logs
    the event. If the reset is not successful or an error occurs, the function
    displays an appropriate error message in the text box and logs the event.

    Args:
        txt_box: The text box widget used to display messages.
        args: Parsed command line arguments.

    Returns:
        None
    """
    log = setup(args)

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
