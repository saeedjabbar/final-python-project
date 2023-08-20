import inspect
import logging
import time
import os


def custom_logger(log_level=logging.DEBUG):
    # Preparation work for creating directory and file
    filename = str(round(time.time() * 1000)) + ".log"
    logs_directory = "../logs/"
    relative_filename = logs_directory + filename # ../logs/filename_random.log
    current_directory = os.path.dirname(__file__)
    destination_file = os.path.join(current_directory, relative_filename)
    # /users/username/Documents/SeleniumPythonProjectMay2023/utilities/../logs/filename_random.log
    # /users/username/Documents/SeleniumPythonProjectMay2023/logs/filename_random.log
    destination_directory = os.path.join(current_directory, logs_directory)
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Set up the logger
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # By default, log all messages
    logger.setLevel(log_level)
    file_handler = logging.FileHandler(destination_file, mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
