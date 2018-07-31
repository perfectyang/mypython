import json
data = []
with open('area2.json', 'r+', encoding='utf-8') as f:
    aa = json.loads(f.read())
    province_data = aa['province_data']
    city_data = aa['city_data']
    area_data = aa['area_data']

    for province in province_data:
        province['show'] = 1
        for city in city_data:
            if province['value'] == int(city):
                for d in city_data[city]:
                    d['show'] = 1
                province['children'] = city_data[city]
                data.append(province)
    # print('data', data)
    for singleData in data:
        if singleData['children']:
            for city in singleData['children']:
                for area in area_data:
                    if city['value'] == area:
                        tem = area_data[city['value']]
                        for d in tem:
                            d['show'] = 1
                        city['children'] = tem
    print('data----', data)
with open('area5.json', 'w+', encoding='utf-8') as fs:
    fs.write(str(data))
