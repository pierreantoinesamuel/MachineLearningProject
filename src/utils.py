import utils as utils
import os


def create_directory(directory):
    """
    Creates a directory if it does not already exist.

    Args:
        directory (str): The path of the directory to create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        utils.log(f"Directory created: {directory}")
    else:
        utils.log(f"Directory already exists: {directory}")