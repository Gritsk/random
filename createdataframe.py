import os
import json
from collections import defaultdict
PREDATOR = "predator"
directory = 'cleanedData/predatory'
NONPREDATOR = 'nonpredator'
directorytwo = 'cleanedData/nonpredatory'
# items=()
d = {'X': [], 'Y': []}
# print(type(items))
for filename in os.listdir(directory):
    print(filename)
    alltext = open(directory+'/'+filename)
    # print(alltext)
    print("**************************")
    allitext = alltext.read()
    # print(allitext)
    d['X'].append(allitext)
    d['Y'].append(PREDATOR)
for filename in os.listdir(directorytwo):
    print(filename)
    alltext = open(directorytwo+'/'+filename)
    # print(alltext)
    print("**************************")
    allitext = alltext.read()
    # print(allitext)
    d['X'].append(allitext)
    d['Y'].append(NONPREDATOR)

with open('dataorganaized.json', 'w') as jsonfile:
    json.dump(d, jsonfile)

print(d['Y'])
print(d['X'])
