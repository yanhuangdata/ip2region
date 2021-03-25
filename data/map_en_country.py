import json

country_mapping = None
with open('country_mapping.json') as map_file:
    country_mapping = json.load(map_file)

country_mapping_dict = {}

for k,v in country_mapping.items():
    if v not in country_mapping_dict.keys():
        country_mapping_dict[v] = k

from_file = open('ip.merge.txt', 'r')
to_file = open('new.ip.merge.txt', 'w')

for line in from_file:
    data = line.strip()
    keys = data.split('|')
    country_ch = keys[2]

    new_line = None
    if (country_ch in country_mapping_dict.keys()):
        country_en = country_mapping_dict[country_ch]
        new_line = data + '|' + country_en
    else:
        print(country_ch)
        new_line = data + '|0'
    to_file.write(new_line)
    to_file.write('\n')

from_file.close()
to_file.close()
