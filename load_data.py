import requests


def data(city, day):
    API_KEY = '4e558506ceac6686360f2710261afab3'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={API_KEY}'

    response = requests.get(url)
    data_json = response.json()
    # print(data_json["list"][16]["weather"])
    day_update = 8 * day
    # dict --> list --> dict
    main_data = data_json["list"][:day_update]
    """
    1 day == 24h -- update 8 lan ( 3h - 1 lan)
    2 day        -- update 16 lan    
    """
    return main_data


if __name__ == "__main__":
    data("Saigon", 2)



