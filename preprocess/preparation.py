from json import JSONDecodeError
import json
import io

def load_config():
    path = 'preprocess/config.json'
    
    try:
        with open(path) as file:
            config = json.load(file)
    except FileNotFoundError:
        print('File not found: {}'.format(path))
        raise
    except JSONDecodeError:
        print('Malformed json: {}'.format(path))
        raise
        
    return config

def load_structures(lang='es'):
    path = 'preprocess/structures.json'
    
    try:
        with io.open(path, 'r', encoding='utf-8') as file:
            structures = json.load(file)[lang]
    except FileNotFoundError:
        print('File not found: {}'.format(path))
        raise
    except JSONDecodeError:
        print('Malformed json: {}'.format(path))
        raise
    except KeyError:
        print('Unnsuported language: {}'.format(language))
        raise 
    return structures