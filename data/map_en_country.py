import json

country_mapping = None
with open('country_mapping.json') as map_file:
    country_mapping = json.load(map_file)

country_mapping_dict = {}

for k,v in country_mapping.items():
    if v not in country_mapping_dict.keys():
        country_mapping_dict[v] = k

# origin:  39.144.0.0|39.144.0.255|中国|山东省|菏泽市|移动
# target: 39.144.0.0|39.144.0.255|中国|0|山东省|菏泽市|移动|China
from_file = open('ipv4_source.txt', 'r')
to_file = open('new.ipv4_source.txt', 'w')

for line in from_file:
    data = line.strip()
    keys = data.split('|')
    country_ch = keys[2]

    keys.insert(3, '0')  # insert a placeholder for region
    # keys.append
    if (country_ch in country_mapping_dict.keys()):
        country_en = country_mapping_dict[country_ch]
        # new_line = data + '|' + country_en
        keys.append(country_en)
    else:
        print(country_ch)
        # new_line = data + '|0'
        keys.append('0')
    new_line = '|'.join(keys)


    to_file.write(new_line)
    to_file.write('\n')

from_file.close()
to_file.close()
