# Check folder with path
# import os
# print(os.getcwd())
  
import simplejson as json
  
f = open('test.json')
data = json.load(f)
filter = data['symbols'][0]['filters']
result = []

for value in filter:
    if 'stepSize' in value.keys():
        result.append(value['stepSize'])

print(result)