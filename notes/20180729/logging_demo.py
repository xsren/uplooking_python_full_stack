import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("endlesscode")
formatter = logging.Formatter('[%(name)-12s %(asctime)s %(levelname)-8s]: %(message)s', '%a, %d %b %Y %H:%M:%S',)
file_handler = logging.FileHandler("test.log")
# file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

import pdb
pdb.set_trace()
"""
l
n
c
p
"""
s = '0'
n = int(s)
logging.info('n = %d' % n)
logger.info('n = %d' % n)
print(10 / n)