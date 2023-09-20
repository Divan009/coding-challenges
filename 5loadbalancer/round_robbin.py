import logging 


class RoundRobbinLB:
    def __init__(self, servers):
        # list of servers
        self.servers = servers
        self.current_index = 0

    def get_next_server(self):
        print(self.current_index)
        # Retrieves the server at the current index from the list of servers.
        server = self.servers[self.current_index]
        self.current_index = (self.current_index+1) % len(self.servers)
        return server