import os
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def copy_directory(src, dst):
    #Recursively copies all contents from the source directory to the destination directory.#
    
    # Check if source directory exists
    if not os.path.exists(src):
        logging.error(f"Source directory {src} does not exist.")
        return
    
    # If destination directory exists, remove it (delete all contents)
    if os.path.exists(dst):
        logging.info(f"Clearing destination directory {dst}.")
        shutil.rmtree(dst)
    
    # Create the destination directory again
    os.mkdir(dst)
    
    # Start copying all files and directories recursively
    _copy_recursively(src, dst)

def _copy_recursively(src, dst):
    #Helper function that recursively copies files and subdirectories.#
    # Get the list of all files and directories in the source directory
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)

        if os.path.isdir(src_item):
            # If item is a directory, create it in the destination and copy its contents
            logging.info(f"Copying directory {src_item} to {dst_item}.")
            os.mkdir(dst_item)
            # Recur for the subdirectory
            _copy_recursively(src_item, dst_item)
        elif os.path.isfile(src_item):
            # If item is a file, copy it to the destination
            logging.info(f"Copying file {src_item} to {dst_item}.")
            shutil.copy(src_item, dst_item)

