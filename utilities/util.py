import random, string, time, os
from utilities.custom_logger import custom_logger


class Util(object):
    log = custom_logger()

    def get_alpha_numeric(self, length, type="letters"):
        """
        Get random string of characters
        :param length: Length of the string, number of characters
        :param type: Type of characters, letters/lower/upper/digits/mix
        :return: string
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def verify_text_contains(self, actual_text, expected_text):
        self.log.info(f"Actual text from application: {actual_text}")
        self.log.info(f"Expected text from application: {expected_text}")
        if expected_text in actual_text:
            self.log.info("Verification Contains !!!")
            return True
        else:
            self.log.error("Verification Does Not Contain !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):
        self.log.info(f"Actual text from application: {actual_text}")
        self.log.info(f"Expected text from application: {expected_text}")
        if expected_text == actual_text:
            self.log.info("Verification Contains !!!")
            return True
        else:
            self.log.error("Verification Does Not Contain !!!")
            return False

    def get_random_timestamp_name(self):
        timestamp = time.time()
        readable_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp))
        return readable_timestamp

    def create_directory(self, directory_name):
        # Preparation work for creating directory and file
        current_directory = os.path.dirname(__file__)
        destination_directory = os.path.join(current_directory, directory_name)
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        return destination_directory
