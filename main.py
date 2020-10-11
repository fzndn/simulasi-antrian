from Server import *
from System import *

import random

def main(number_of_customer):
    ali = Ali()
    badu = Badu()
    system = System([ali, badu])

    for i in range(number_of_customer):
        random_digit_car = random.randint(1, 100)
        random_digit_service = random.randint(1, 100)

        system.car_arrival(random_digit_car, random_digit_service)

    ali.print_log()
    badu.print_log()
