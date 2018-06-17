def distance(origin, destination, defense):    
    origin=[int(c) for c in origin[1:-1].split(':')]
    destination=[int(c) for c in destination[1:-1].split(':')]
    distance=float('inf')
    
    if defense:
        distance = abs(origin[0]-destination[0])*10000
        distance += abs(origin[1]-destination[1])*10
        distance += abs(origin[2]-destination[2])
        
    return distance

def resources(ratio, resource,defense):
    metal=int(resource['metal'].replace('.',''))
    crystal=int(resource['crystal'].replace('.',''))
    deuteryum=int(resource['deuteryum'].replace('.',''))
    all_resources=0
    
    if defense:
        all_resources += metal*ratio[0] + crystal*ratio[1] + deuteryum*ratio[2]
    
    return all_resources

class Ranking:
    # Defense True means that I do not care if a planet have defense
    def __init__(self, user_id=0, coordinates='[1:1:1]', ratio=[1,2,3], defense=True):
        self.user_id=user_id
        self.coordinates=coordinates
        self.ratio=ratio
        self.defense=defense
        self.my_espionages=[]
    
    # Espionage is a dict
    def add_espionage(self, espionage):
        self.my_espionages.append(espionage)
        
    def clear_espionages(self):
        self.my_espionages = []
        
    # espionage['care']!=True or self.defense != False --> It gives False if I care the defenses and the planet have defenses
    def ranking_clossnes(self):
        return sorted(self.my_espionages, key=lambda espionage: (distance(self.coordinates,espionage['coordinates'], espionage['care']!=True or self.defense != False),distance(self.coordinates, espionage['coordinates'], True)))
    
    def ranking_resources(self):
        return sorted(self.my_espionages, key=lambda espionage: (resources(self.ratio,espionage['resources'],espionage['care']!=True or self.defense != False), resources(self.ratio, espionage['resources'], True)), reverse=True)
    
    def get_all(self):
        return self.my_espionages