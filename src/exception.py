import sys

def error_message_details(error,error_datails:sys):
   
    _,_,exc_tb = error_datails.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    print(f"the file name is {file_name}")
    error_message = f"Error occured in python script name[{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_datails=error_details)

    def __str__(self):
        return self.error_message    