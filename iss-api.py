# Command line tool to get information about the international space station 
# and the people on board from http://api.open-notify.org/

# Author: Cale Workman
# Date: 7/22/2020

import sys
import json
import datetime
import itertools
import urllib.request
from operator import itemgetter

base_api_url = 'http://api.open-notify.org'

def loc():    
    """Print the location of the ISS as a (latitude, longitude) pair."""
    
    url = base_api_url + '/iss-now.json'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        position = data['iss_position']
        latitude = position['latitude']
        longitude = position['longitude']
        now = datetime.datetime.now();
        
        print('The ISS current location at {} is ({}, {}).'.format(now, latitude, longitude))
        
        
def passing(lat, long):
    """Print the passing details of the ISS for a given latitude and longitude."""
        
    url = base_api_url + '/iss-pass.json?lat={}&lon={}'.format(lat, long)
        
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        
        passes = data['response']
        for p in passes:
            date_time = datetime.datetime.fromtimestamp(p['risetime']).strftime("%H:%M:%S on %m/%d/%Y")
            duration = p['duration']
            print('The ISS will be overhead at ({}, {}) at {} for {} seconds.'.format(lat, long, date_time, duration))
    
    
def people():
    """Print names of the people currently in space, grouped by spacecraft."""
    
    url = base_api_url + '/astros.json'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        people = data['people']
        
        for key, value in itertools.groupby(people, key=itemgetter('craft')):
            craft = key
            people_on_craft = [person['name'] for person in value]
            print('People on the {}: {}'.format(craft, ', '.join(people_on_craft)))
    

def call_function(function, args):
    """Call the appropriate function."""   
    
    func = function.lower()
    
    if func == 'loc':
        loc()
        
    elif func == 'pass':
        try:
            latitude = args[0]
            longitude = args[1]
        except IndexError:
            print('Latitude and longitude are required.')
        else:
            passing(latitude, longitude)
        
    elif func == 'people':
        people()
        
    else:
        print('Improper function call. Possible functions are \'loc\', \'pass\', or \'people\'.')

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)  # Pop off the file name
    
    if len(args) == 0:
        func = input('Please supply a function name.')
    else:
        func = args.pop(0)
        
    call_function(func, args)

