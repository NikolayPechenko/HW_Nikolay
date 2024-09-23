import logging

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f'Podelili {a} na {b} s kaifom')
        return a / b
    except ZeroDivisionError as error:
        logging.error(f'Gay!', exc_info=True)
        return 0


def sqrt(a):
    try:
        if a > 0:
            logging.info(f's kaifom izvlekli koreny iz {a}')
            return a ** 0.5
        else:
            0 / 0
    except:
        logging.error(f'Gay!, otricatelnoe chislo', exc_info=False)
        return 0


def pow(a, b):
    return a**b


if __name__ == '__main__':
    # logging.debug()
    # logging.info()
    # logging.warning()
    # logging.error()
    # logging.critical() - распределены по уровню важности (критичности)
    logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                        format='%(asctime)s | %(levelname)s |  %(message)s')


print(__name__)


