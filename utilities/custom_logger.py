# logging.basicConfig(filename="test.log", level=logging.DEBUG)
# logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
# datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


import logging
import inspect



def customLogger(loglevel=logging.DEBUG):

    # gets the name of the class/method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to info
    handler = logging.FileHandler("automation.log", mode="a")
    handler.setLevel(loglevel)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p')

    # and formatter to console handler -> chandler
    handler.setFormatter(formatter)

    # add console handler to logger
    logger.addHandler(handler)

    return logger