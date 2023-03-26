import os
from datetime import date
from tkinter import messagebox
from _logger import logger_handler as _log


# Configure logging settings
log = _log

# Define the execute function to be called when the user clicks the Execute button
def execution_logic(src_path: str, tgt_path: str, file_ext: str, del_src: str) -> None:
    try:
        # Get the values of the input fields and checkbox
        # source dir path
        v_source_dir = os.path.expanduser(src_path)
        # base for target dir
        v_base_dir = os.path.expanduser(tgt_path)
        # file extension
        file_ext = file_ext
        # delete flag
        delete_source = del_src

        ### Execution logic ###
        # target dir path
        v_target_dir = f"{v_base_dir}/_auto_{date.today().strftime('%d.%m.%Y')}"

        # get folders that start with "IMG_"
        v_folders = [f for f in os.listdir(
            v_source_dir) if f.startswith("IMG_")]

        # create new folder in target dir if it doesn't exist
        if not os.path.exists(v_target_dir):
            os.makedirs(v_target_dir)

        # loop through folders and move files to target dir
        # !!! default file extension is defined in config file
        for v_folder in v_folders:
            v_files = [f for f in os.listdir(
                v_source_dir+"/"+v_folder) if f.endswith(file_ext)]
            for v_file in v_files:
                os.rename(f"{v_source_dir}/{v_folder}/{v_file}",
                          f"{v_target_dir}/{v_file}")

        # delete files in folders in source dir
        for v_folder in v_folders:
            v_files = [f for f in os.listdir(v_source_dir+"/"+v_folder)]
            for v_file in v_files:
                os.remove(f"{v_source_dir}/{v_folder}/{v_file}")

        # send to recycle bin folders in source dir
        if delete_source:
            for v_folder in v_folders:
                os.system(f"rm -rf {v_source_dir}/{v_folder}")
    except Exception as err:
        log(err)
        messagebox.showerror("Error", err)
