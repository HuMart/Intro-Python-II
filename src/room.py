# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''
        self.path = []

    def __repr__(self):
        return ''+self.name+''+self.desc+''
    def __str__(self):
        return ''+self.name+''+self.desc+''

    def check_path(self):
        self.paths = [{"north": self.n_to, "south": self.s_to, "east": self.e_to, "west": self.w_to}]
        routes = []
        for p in self.path:
            for r in p:
                if p[r]!='':
                    routes.append(p[r])
        return routes

