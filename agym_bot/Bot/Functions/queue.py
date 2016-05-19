import datetime
from .utilities import json_file

def events(event, date):
    f=json_file.write('../Data/queue.json')
    f['event(id)']=date


def delete(date):
    f=json_file.read('../Data/queue.json')
    for key in f:
    	if f[key]==datetime.today():
    		del(f[key])