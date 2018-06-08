def read_espionage(espionage, lang='es'):
    if lang == 'es':
        ans = read_espionage_spanish(espionage)
    return ans

def read_espionage_spanish(espionage):
    ans = {}
    
    espionage = espionage.split('\n')
    line = espionage[0].split(' ')
    ans.update({'planet':line[4]})
    ans.update({'coordinates':line[5]})
    ans.update({'date':'{} {}'.format(line[6], line[7])})
    
    i = 1
    # I want to find the line with his name
    while espionage[i][0] != 'J':
        i+=1
    ans.update({'name':' '.join(espionage[i].split(' ')[1:])[1:]})
    
    i+=1
    ans.update({'counterspionage':espionage[i].split(' ')[3]})
    
    i+=3
    line = espionage[i].split(' ')
    ans.update({'metal':line[0]})
    ans.update({'crystal':line[1]})
    ans.update({'deuteryum':line[2]})
    ans.update({'energy':line[3]})
    
    i+=2
    
    return ans