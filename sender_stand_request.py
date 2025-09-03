import requests
import configuration          
import request_data  

#Создание заказа
def post_new_order(body):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.post(url, json=body)

# Получить заказ по треку ?t=...
def get_track_order(track):
    url = configuration.URL_SERVICE + configuration.GET_TRACK
    return requests.get(url, params={"t": str(track)})