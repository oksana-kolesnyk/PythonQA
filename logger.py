import logging


class Logger:
    
    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.formatter = None
    
    def get_logger(self, __name__):
        self.logger = logging.getLogger(__name__)
        return self.logger
    
    def init_logger_config(self):
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(self.formatter)
        
        file_handler = logging.FileHandler('logfile.log')
        file_handler.setFormatter(self.formatter)
        
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        
    
    