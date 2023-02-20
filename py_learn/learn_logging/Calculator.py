import logging

import Employee

from Employee import log_path
emp_log = log_path + "/emp_log"
logging.basicConfig(filename=emp_log,
                    level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s :  %(message)s')


def add(x, y):
    return x + y


x, y = 10, 20
#logging.info('add: {} + {} = {}'.format(x, y, add(x, y)))
logging.info('add: {} + {} = {}'.format(x, y, add(x, y)))
