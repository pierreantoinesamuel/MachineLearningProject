import sys
from src.logs import logging


def error_message_detail(error, error_details:sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_details:sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_details)

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return CustomException.__name__.str() + self.error_message
    

# Uncomment the following lines to test the CustomException class


# if __name__ == "__main__":
#     try:
#         raise ValueError("This is a test error")
#     except Exception as e:
#         logging.error(CustomException(e, sys))
#         print(CustomException(e, sys))
    

#     try:
#         raise TypeError("This is another test error")
#     except Exception as e:
#         logging.error(CustomException(e, sys))
#         print(CustomException(e, sys))
#         logging.error(CustomException(e, sys))

#     try:
#         raise IndexError("This is yet another test error")  
#     except Exception as e:
#         logging.error(CustomException(e, sys))
#         print(CustomException(e, sys))
#         logging.error(CustomException(e, sys))
#         logging.error(CustomException(e, sys))

#     try:
#         numb = 10/0  # This will raise a ZeroDivisionError
#         raise ValueError("This is a test error")
#     except Exception as e:
#         logging.error(CustomException(e, sys))
#         logging.info(CustomException(e, sys))