# Allows us to read a espionage
def read_espionage(espionage, structures):
    ans = {}
    carefull = False
    
    espionage = espionage.split('\n')
    line = espionage[0].split(' ')
    
    j = 4
    while line[j][0] != '[':
        j += 1
    ans.update({'planet':' '.join(line[4:j])})
    ans.update({'coordinates':line[j]})
    ans.update({'date':'{} {}'.format(line[j+1], line[j+2])})
    
    i = 2
    name = ' '.join(espionage[i].split(' ')[1:])[1:]
    pos = name.find('(')    
    
    if pos != -1:
        name = name[:pos]
    
    ans.update({'name':name})
    ans.update({'inactive':pos!=-1})
    
    i += 1
    ans.update({'counterspionage':espionage[i].split(' ')[3]})
    
    i += 3
    line = espionage[i].split(' ')
    resources = {}
    resources.update({'metal':line[0]})
    resources.update({'crystal':line[1]})
    resources.update({'deuteryum':line[2]})
    resources.update({'energy':line[3]})
    ans.update({'resources':resources})
    
    pipeline = ['ships','defense','buildings','research']
    
    for element in pipeline:
        i += 2
        line = espionage[i].replace('.','')
        care, entities = read_entities(line,structures[element])
        if care:
            carefull = True
        ans.update({element:entities})
    
    ans.update({'care':carefull})
    
    return ans

def read_entity(structure,line):
    num_structure = 0
    #print(':' + structure + ': ---> :' + line[:len(structure)] + ':')
    if structure == line[:len(structure)]:
        line = line[len(structure)+1:]
        j = 1
        while j-1 < len(line) and line[:j].isdigit():
            j += 1
        num_structure = int(line[:j-1])
        line = line[j-1:]
        
    return line, num_structure

def read_entities(line, structure):
    ans = {}
    length = len(line)
    while line != '':
        for s in structure:
            line, num = read_entity(structure[s], line)
            if num != 0:
                ans.update({s:num})
        if len(line) == length:
            break;
    
    return len(ans) == 0, ans