# Check folder with path
# import os
# print(os.getcwd())
  
import simplejson as json
  
# Khi load từ file
f = open('test.json')
data = json.load(f)

# Khi load từ API và có được json
# f = '{"name": "Bob", "languages": "English"}'
# data = json.loads(f)

filter = data['symbols'][0]['filters']
result = []

for value in filter:
    if 'stepSize' in value.keys():
        if value['filterType'] == 'LOT_SIZE':
            result.append(value['stepSize'])

print(result)