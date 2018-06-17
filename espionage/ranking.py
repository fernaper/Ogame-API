def distance(origin, destination, defense):    
    origin=[int(c) for c in origin[1:-1].split(':')]
    destination=[int(c) for c in destination[1:-1].split(':')]
    distance=100000
    
    if defense:
        distance = abs(origin[0]-destination[0])*10000
        distance += abs(origin[1]-destination[1])*10
        distance += abs(origin[2]-destination[2])
        
    return distance

def resources(ratio, resource, defense):
    metal=int(resource['metal'].replace('.',''))
    crystal=int(resource['crystal'].replace('.',''))
    deuteryum=int(resource['deuteryum'].replace('.',''))
    all_resources=1
    
    if defense:
        all_resources = metal*ratio[0] + crystal*ratio[1] + deuteryum*ratio[2]
    
    return all_resources

def generic(origin, destination, ratio, resource, defense):
    # Numbers between 0 and 1
    cost = distance(origin,destination,defense)/100000.0
    cost += 1 - (1.0/resources(ratio,resource,defense))
    return cost/2.0

def new_date(old_date, new_date):
    old_date = old_date.split(' ')
    new_date = new_date.split(' ')
    
    old_day = list(map(int,old_date[0].split('.')))
    new_day = list(map(int,new_date[0].split('.')))
    
    for i in range(2,-1,-1):
        if old_day[i] < new_day[i]:
            return True
        elif old_day[i] > new_day[i]:
            return False
    
    old_hour = old_date[1].split(':')
    new_hour = new_date[1].split(':')
    
    for i in range(3):
        if old_hour[i] < new_hour[i]:
            return True
        elif old_hour[i] > new_hour[i]:
            return False
    
    return False

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
        for i in range(len(self.my_espionages)):
            if espionage['coordinates'] == self.my_espionages[i]['coordinates']:
                if new_date(self.my_espionages[i]['date'], espionage['date']):
                    self.my_espionages[i] = espionage
                return
            
        self.my_espionages.append(espionage)
        
    def clear_espionages(self):
        self.my_espionages = []
        
    # espionage['care']!=True or self.defense != False --> It gives False if I care the defenses and the planet have defenses
    def ranking_clossnes(self):
        return sorted(self.my_espionages, key=lambda espionage: (distance(self.coordinates,espionage['coordinates'], espionage['care']!=True or self.defense != False),distance(self.coordinates, espionage['coordinates'], True)))
    
    def ranking_resources(self):
        return sorted(self.my_espionages, key=lambda espionage: (resources(self.ratio,espionage['resources'],espionage['care']!=True or self.defense != False), resources(self.ratio, espionage['resources'], True)), reverse=True)
    
    def ranking_generic(self):
        return sorted(self.my_espionages, key=lambda espionage: (generic(self.coordinates, espionage['coordinates'], self.ratio, espionage['resources'], espionage['care']!=True or self.defense != False), generic(self.coordinates, espionage['coordinates'], self.ratio, espionage['resources'], True)), reverse=True)
    
    def get_all(self):
        return self.my_espionages