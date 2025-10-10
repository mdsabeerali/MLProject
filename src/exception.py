# Shows errors in a clean and understandable way.
# Tells which file, line number, and reason caused the error.
# You can create custom error messages.
"""
Benefits:
✅ Easier to find and fix mistakes.
✅ Prevents the program from crashing badly.
✅ Gives clear messages during debugging or deployment.
✅ Makes the project more reliable and safe.
"""
import sys
from src.logger import logging
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
    def __str__(self):
        return self.error_message
