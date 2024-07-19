import logging
import logging.handlers
import datetime

def create_logger():
    logger=logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)


    demo_handler=logging.handlers.TimedRotatingFileHandler(filename='./logs/logging_demo_0.log',when='D',interval=1,backupCount=7)
    demo_handler.setLevel(logging.DEBUG)
    demo_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


    error_handler=logging.FileHandler(filename='./logs/error_0.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


    logger.addHandler(demo_handler)
    logger.addHandler(error_handler)
    return logger


if __name__ == '__main__':
    logger=create_logger()
    #logging.basicConfig(filename='./logs/logging_demo.log', level=logging.DEBUG,
                        #format='%(asctime)s - %(levelname)s - %(message)s-%(module)s-%(funcName)s-%(lineno)d')
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


