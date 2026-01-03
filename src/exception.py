import sys
from src.logger import logging

def custom_error_exception(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line = exc_tb.tb_lineno
    error_message = f"the error occured in python script [{filename}] at line no [{line}] the error : [{str(error)}]"

    return error_message

class customException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = custom_error_exception(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message

if __name__ == '__main__':

    try:
        a = 1/0

    except Exception as e:
        logging.info('devide by zero')
        raise customException(e,sys)