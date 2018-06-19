'''
OGame Api Server.

Usage:
  Server.py [--app=<application>] [--server=<adapter>] [--host=<h>] [--port=<p>] [--reloader=<r>] [--interval=<i>] [--quiet=<q>] [--options=<o>] [--debug=<d>]
  Server.py (-h | --help)

Options:
  -h --help              Show this screen.
  --version              Show version.
  --app=<application>    WSGI application or target string supported by load_app().[default: default_app()])
  --server=<adapter>     Server adapter to use. See server_names keys for valid names or pass a ServerAdapter subclass. [default: wsgiref]
  --host=<h>             Server address to bind to. Pass 0.0.0.0 to listens on all interfaces including the external one. [default: 127.0.0.1]
  --port=<p>             Server port to bind to. Values below 1024 require root privileges. [default: 8080]
  --reloader=<r>         Start auto-reloading server? [default: False]
  --interval=<in>        Auto-reloader interval in seconds [default: 1]
  --quiet=<q>            Suppress output to stdout and stderr? [default: False]
  --options=<o>          Options passed to the server adapter.
  --debug=<d>            Debug mode. [default: False]

'''
from preprocess import preparation
from espionage import espionage as spy
from espionage import ranking
from mydata import base
import io
import os.path
import json
from bottle import run, get, post, request
from docopt import docopt

@post('/ogame/espionage')
def espionage():
    espionage = request.forms.get('text')
    config = preparation.load_config()
    structures = preparation.load_structures(lang=config['language'])
    analysis = spy.read_espionage(espionage, structures)
    print(analysis)
    dump = json.dumps(analysis)
    with io.open('espionage/my_spy/{}-{}.json'.format(analysis.get('name'), analysis.get('planet')),"w", encoding='utf-8') as my_spy:
        my_spy.write(dump)
    
    return analysis

@post('/ogame/ranking/<rank>')
def ranking(rank='generic'):
    data = request.json.get('data')
    defense = request.json.get('defense')
    config = preparation.load_config()
    structures = preparation.load_structures(lang=config['language'])
    r = ranking.Ranking(defense=defense)
    
    for espionage in data:
        analysis = spy.read_espionage(espionage,structures)
        r.add_espionage(analysis)
        
    if rank=='generic':
        return r.ranking_generic()
    elif rank=='clossnes':
        return r.ranking_clossnes()
    elif rank=='resources':
        return r.ranking_resources()
    else:
        return r.get_all()

if __name__ == "__main__":
    arguments = docopt(__doc__)
    
    # We can not specify the app parameter
    run(server=arguments.get('--server'),
        host=arguments.get('--host'), port=arguments.get('--port'),
        reloader=arguments.get('--reloader')=='True', interval=int(arguments.get('--interval')),
        quiet=arguments.get('--quiet')=='True',debug=arguments.get('--debug')=='True')