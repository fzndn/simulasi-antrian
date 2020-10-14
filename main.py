from Server import *
from System import *

import csv
import random

def simulate(number_of_customer):
    system = System([Ali(), Badu()])

    for i in range(number_of_customer):
        random_digit_car = random.randint(1, 100)
        random_digit_service = random.randint(1, 100)

        system.service(random_digit_car, random_digit_service)

    with open('simulasi_antrian.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(system.get_log())
