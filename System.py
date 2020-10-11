class System(object):
    def __init__(self, servers):
        self.customer = 0
        self.arrival_time = 0
        self.servers = servers
        
    def car_arrival(self, random_digit_car, random_digit_service):
        interarrival_time = self.get_interarrival_time(random_digit_car)
        
        if self.customer != 0:
            self.arrival_time += interarrival_time
            
        self.service(random_digit_service)      
            
    def service(self, random_digit_service):
        self.customer += 1
        servers = self.servers
        server = None
        if servers[0].get_time_service_ends() <= self.arrival_time:
            server = servers[0]
        elif servers[0].get_time_service_ends() <= servers[1].get_time_service_ends():
            server = servers[0]
        else:
            server = servers[1]

        service_time = server.get_service_time(random_digit_service)
        old_time_service_ends = server.get_time_service_ends()

        time_service_begin = self.arrival_time if old_time_service_ends <= self.arrival_time else old_time_service_ends
        time_customer_wait_in_queue = time_service_begin - self.arrival_time
        time_service_ends = time_service_begin + service_time
        time_customer_spends_in_system = time_service_ends - self.arrival_time
        idle_time = 0 if self.customer == 0 else time_service_begin - old_time_service_ends

        server.add_log(
            (self.customer,
             time_service_begin,
             time_customer_wait_in_queue,
             time_service_ends,
             time_customer_spends_in_system,
             idle_time)
        )

        server.set_time_service_ends(time_service_ends)
        
    def get_interarrival_time(self, random_digit_car):
        if random_digit_car >= 1 and random_digit_car <= 25:
            return 1
        elif random_digit_car >= 26 and random_digit_car <= 65:
            return 2
        elif random_digit_car >= 66 and random_digit_car <= 85:
            return 3
        return 4
