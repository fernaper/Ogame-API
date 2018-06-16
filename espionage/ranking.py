def distance(origin, destination):
    origin=[int(c) for c in origin[1:-1].split(':')]
    destination=[int(c) for c in destination[1:-1].split(':')]
    distance = abs(origin[0]-destination[0])*10000
    distance += abs(origin[1]-destination[1])*10
    distance += abs(origin[2]-destination[2])
    
    return distance

class Ranking:
    def __init__(self, user_id=0, coordinates='[1:1:1]'):
        self.user_id=user_id
        self.coordinates=coordinates
        self.my_espionages=[]
    
    # Espionage is a dict
    def add_espionage(self, espionage):
        self.my_espionages.append(espionage)
        
    def clear_espionages(self):
        self.my_espionages = []
        
    def ranking_clossnes(self):
        return sorted(self.my_espionages, key=lambda espionage: distance(self.coordinates,espionage['coordinates']))
    
    def get_all(self):
        return self.my_espionages