# import json
# for ISP
from translate import Translator
# for geo names
from argostranslate import package, translate

package.update_package_index()
available_packages = package.get_available_packages()
zh_en_package = next(p for p in available_packages if p.from_code == "zh" and p.to_code == "en")
package.install_from_path(zh_en_package.download())

isp_translator = Translator(to_lang="en", from_lang="zh")

geo_cache = {}
isp_cache = {'移动':'China Mobile', '联通':'China Unicom', '电信':'China Telecom', '铁通':'China Tietong', '鹏博士':'Dr. Peng Telecom'}

# origin:  39.144.0.0|39.144.0.255|中国|山东省|菏泽市|移动
# target: 39.144.0.0|39.144.0.255|中国|0|山东省|菏泽市|移动|China|0|shandong|Heze|China Mobile
from_file = open('ipv4_source.txt', 'r')
to_file = open('new.ipv4_source.txt', 'w')

line_count = 0
for line in from_file:
    line_count += 1
    if (line_count % 1000 == 0):
        print(f"processed {line_count} lines")

    data = line.strip()
    keys = data.split('|')
    country_ch = keys[2]

    keys.insert(3, '0')  # insert a placeholder for region


    # range 2 to 4 for country and region
    for i in range(2,6):
        name_ch = keys[i]
        if (any(char for char in name_ch if '\u4e00' <= char <= '\u9fff')):
            if (name_ch in geo_cache.keys()):
                name_en = geo_cache[name_ch]
            else:
                name_en = translate.translate(name_ch, "zh", "en")
            if (any(char for char in name_en if '\u4e00' <= char <= '\u9fff')):
                print(name_ch + " -> " + name_en)
            geo_cache[name_ch] = name_en
            keys.append(name_en)
        else:
            keys.append(name_ch)


    #translate isp name
    isp_ch = keys[6]
    if (any(char for char in isp_ch if '\u4e00' <= char <= '\u9fff')):
        if (isp_ch in isp_cache.keys()):
            isp_en = isp_cache[isp_ch]
        else:
            isp_en = isp_translator.translate(isp_ch)
        if (any(char for char in isp_en if '\u4e00' <= char <= '\u9fff')):
            print(isp_ch + " -> " + isp_en)
        isp_cache[isp_ch] = isp_en
        keys.append(isp_en)
    else:
        keys.append(isp_ch)

    new_line = '|'.join(keys)
    
    to_file.write(new_line)
    to_file.write('\n')

from_file.close()
to_file.close()
