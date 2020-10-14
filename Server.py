class Server(object):
    def __init__(self, name):
        self.name = name
        self.time_service_ends = 0

    def get_service_time(self, random_digit):
        pass

    def get_time_service_ends(self):
        return self.time_service_ends

    def set_time_service_ends(self, tse):
        self.time_service_ends = tse

    def get_name(self):
        return self.name

        
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
