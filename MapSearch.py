import requests
import json
import types
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

GoogleKey = "" # Free service allows maximum 150000 requests every 24 hours. You need pay if you want more


def Get_Detail_by_ID(place_id):
    '''
    get the detail of a place according to its place_id
    
    call example: the parameter is the one place_id
    >>> Get_Detail_by_ID("ChIJlfjVd0IayUwRi8rjxbMESlI")
    
    :param place_id: 
    :return: a map containing 
    '''
    url = "https://maps.googleapis.com/maps/api/place/details/json?placeid={id}&key={key}".\
        format(id=place_id, key=GoogleKey)
    response = requests.get(url,headers=header,proxies={'https':'socks5://127.0.0.1:1086'})
    # print(url)
    # print(response.text)
    json_response = response.content.decode()
    dict_json = json.loads(json_response)
    result = dict_json['result']
    # print(result['name'],result['formatted_address'])
    returnData = {}
    returnData['name'] = result['name']
    returnData['address'] = result['formatted_address']
    return returnData


def Radar_Search(Lat, Lng, Radius, Type):
    '''
    Search in a given scope, you need to provide a center of circle(lat, lng) , radius of circle and type of targets you want
    Note return maximumly 200 results once thus setting radius oversize makes no sense
    
    >>> data = Radar_Search(lat="45.50478469999999", lng="-73.57715109999999", radius="200", type="restaurant")
    
    :param Lat: Latitude, example: 45.50478469999999
    :param Lng: Longitude, example: -73.57715109999999, negative means the west of earth
    :param Radius: Search radious, example: 1000 (unit: meter)
    :param Type: type of targets, example: parking, restaurant, university and so on
    :return: returnData, which is a List in the format [placeid, lat, lng]
    '''
    url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location={lat},{lng}' \
          '&radius={radius}&type={type}&key={APIkey}'\
        .format(lat=Lat, lng=Lng, radius=Radius, type=Type, APIkey=GoogleKey)
    print(url)
    response = requests.get(url,headers=header,proxies={'https':'socks5://127.0.0.1:1086'})
    json_response = response.content.decode()
    # 将json字符串转换成dic字典对象
    dict_json = json.loads(json_response)
    resultData = dict_json['results']
    returnData = []
    for target in resultData:
        # print(target['place_id'], target['geometry']['location']['lat'], target['geometry']['location']['lng'])
        target_detail = Get_Detail_by_ID(target['place_id'])
        print(target_detail['name'],",", target_detail['address'],",", target['geometry']['location']['lat'],",", target['geometry']['location']['lng'])
        name = target_detail['name'].replace(",",".")
        addr = target_detail['address'].replace(",",".")
        returnData.append((name, addr, target['geometry']['location']['lat'], target['geometry']['location']['lng']))
    print("\nTotal:", len(returnData))
    return returnData


def Get_Postion_by_Address(Address, City, Country):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={address},{city},{country}&key={key}".\
        format(address=Address, key=GoogleKey, city=City, country=Country)
    response = requests.get(url, headers=header, proxies={'https': 'socks5://127.0.0.1:1086'})
    json_response = response.content.decode()
    # 将json字符串转换成dic字典对象
    dict_json = json.loads(json_response)
    resultData = dict_json['results'][0] # A hidden worry. Because there may be more than one place with the same name.
                                         # But I only deal with one case
    lat = resultData['geometry']['location']['lat']
    lng = resultData['geometry']['location']['lng']
    print("Address: "+Address+", ", "City: "+City+", ", "Country: "+Country+", lat and lng: ","\t",lat,lng)
    return lat,lng


def writeList2CSV(myList,filePath):
    '''
    write the list data into a file in the format of csv
    
    >>> writeList2CSV(data, "./data.csv")
    
    :param myList: 
    :param filePath: 
    :return: None
    '''
    try:
        with open(filePath, mode='w+', encoding='utf-8') as file:
            for items in myList:
                for item in items:
                    item = str(item)
                    file.write(item)
                    file.write(",")
                file.write("\n")
    except Exception :
        print(Exception.__traceback__)
        print("Write Error，please check the path of output file and the encoding type of data.")
    finally:
        file.close();# file must be closed after writing


if __name__ == '__main__':
    # lat = "45.50478469999999"
    # lng = "-73.57715109999999" # Actually, it's the geographic position of McGill University
    print("Input Address, City, Country, Type, Radius.\nExample:\nAddress: Zhejiang University\nCity: \t Hangzhou\nCountry: China\nType:\t restaurant\nRadius:\t 1000\n------------------------\n")
    addr = input("Address:")
    city = input("City:")
    country = input("Country:")
    type = input("Type:")   # target tyoe
    radius = int(input("Radius:")) # search radius

    lat, lng = Get_Postion_by_Address(addr, city, country) # it will return lat and lng
    data = Radar_Search(lat, lng, radius, type) # start to search
    writeList2CSV(data, addr+".csv") # write the data into file in the format of csv


