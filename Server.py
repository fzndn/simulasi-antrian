class Server(object):
    def __init__(self, name):
        self.name = name
        self.time_service_ends = 0
        self.service_log = []

    def get_service_time(self, random_digit):
        pass

    def get_time_service_ends(self):
        return self.time_service_ends

    def set_time_service_ends(self, tse):
        self.time_service_ends = tse

    def add_log(self, log):
        self.service_log.append(log)

    def print_log(self):
        print("LOG SERVICE: " + self.name)
        print(" Customer # | Time Service Begins | Time Customer wait in Queue | Time Service Ends | Time Customer Spends in the System | Idle Time of Server ")
        print("------------+---------------------+-----------------------------+-------------------+------------------------------------+---------------------")
        for log in self.service_log:
            print(" {:>10} | {:>19} | {:>27} | {:>17} | {:>34} | {:>19} ".format(log[0], log[1], log[2], log[3], log[4], log[5]))

        
class Ali(Server):
    def __init__(self):
        super().__init__('Ali')

    def get_service_time(self, random_digit):
        if random_digit >= 1 and random_digit <= 30:
            return 2
        elif random_digit >= 31 and random_digit <= 58:
            return 3
        elif random_digit >= 59 and random_digit <= 83:
            return 4
        return 5


class Badu(Server):
    def __init__(self):
        super().__init__('Badu')

    def get_service_time(self, random_digit):
        if random_digit >= 1 and random_digit <= 35:
            return 3
        elif random_digit >= 36 and random_digit <= 60:
            return 4
        elif random_digit >= 61 and random_digit <= 80:
            return 5
        return 6
