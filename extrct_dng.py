#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import tkinter as tk
from tkinter import messagebox
import configparser
from exec_logic import execution_logic as exec_logic

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the default values for the input fields and checkbox from the configuration file
default_source_path = config.get('DEFAULT', 'source_path', fallback='')
default_target_path = config.get('DEFAULT', 'target_path', fallback='')
default_file_ext = config.get('DEFAULT', 'file_ext', fallback='')
default_delete_source = config.getboolean(
    'DEFAULT', 'delete_source', fallback=False)


def main_window():
    # Create a new tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("DNG File Transfer")

    # Configure the column and row weights
    window.columnconfigure(1, weight=1)

    # Set the default window size
    window.geometry("720x200")

    # Create a label and entry widget for the source string path input field
    source_path_label = tk.Label(window, text="Source String Path:")
    source_path_label.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    source_path_entry = tk.Entry(window)
    source_path_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    # Set the default value for the source string path input field from the configuration file
    source_path_entry.insert(0, default_source_path)

    # Create a label and entry widget for the base target string path input field
    target_path_label = tk.Label(window, text="Base Target String Path:")
    target_path_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
    target_path_entry = tk.Entry(window)
    target_path_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

    # Set the default value for the base target string path input field from the configuration file
    target_path_entry.insert(0, default_target_path)

    # Create a label and entry widget for the file extension input field
    file_ext_label = tk.Label(window, text="File Extension:")
    file_ext_label.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
    file_ext_entry = tk.Entry(window)
    file_ext_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

    # Set the default value for the file extension input field from the configuration file
    file_ext_entry.insert(0, default_file_ext)

    # Create a checkbox widget for the delete source folders option
    delete_source_var = tk.BooleanVar()
    delete_source_checkbox = tk.Checkbutton(
        window, text="Delete Source Folders", variable=delete_source_var)
    delete_source_checkbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Set the default value for the delete source folders checkbox from the configuration file
    delete_source_var.set(default_delete_source)

    # Create a button widget for execution
    execute_button = tk.Button(
        window,
        text="Execute",
        command=lambda: exec_logic(
            src_path=source_path_entry.get(),
            tgt_path=target_path_entry.get(),
            file_ext=file_ext_entry.get(),
            del_src=delete_source_var.get()
        ))
    execute_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    # Run the tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    try:
        main_window()
    except Exception as ex:
        messagebox.showerror("Error", f"An error occurred: {ex}")