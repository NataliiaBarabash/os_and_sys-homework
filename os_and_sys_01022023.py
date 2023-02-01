import logging
import sys
import os

os.environ.get('FUNCTION', 'add')

logging.basicConfig(
    filename='test.log',
    filemode='a',
    format='%(asctime)s, %(msecs)d, %(levelname)s, %(name)s, [%(filename)s:%(lineno)d],%(message)s',
    datefmt='%H,%M,%S',
    level=logging.INFO,

)
logger = logging.getLogger()

if __name__ == '__main__':
    try:
        var1, var2 = sys.argv[1:]
    except ValueError:
        logger.exception('Called with: %s', sys.argv[1:])
        exit(2)
    except NameError:
        logger.exception('Called with: %s', sys.argv[1:])
        exit(2)
    except TypeError:
        logger.exception('Called with: %s', sys.argv[1:])
        exit(2)

def add (var1, var2):
    c= int(var1)+int(var2)
    print(c)
    logger.info('Result: %s', sys.argv[1:])

def multiply (var1, var2):
    c= int(var1)*int(var2)
    print(c)
    logger.info('Result: %s', sys.argv[1:])

def take_away (var1, var2):
    c = int(var1) - int(var2)
    print(c)
    logger.info('Result: %s', sys.argv[1:])

def divide (var1, var2):
    c = int(var1) / int(var2)
    print(c)
    logger.info('Result: %s', sys.argv[1:])