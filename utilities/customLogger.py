# import os
# import logging
#
# class LogGen():
#     @staticmethod
#     def loggen(self):
#         path=os.path.abspath(os.curdir)+'\\logs\\automation.log'
#         logging.basicConfig(filename=path,format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.WARN)
#         return logger
import logging
import os


class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir)+'\\logs\\automationmazhar.log'
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
