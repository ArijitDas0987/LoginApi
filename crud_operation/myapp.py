import json
import requests

URL="http://127.0.0.1:8000/Studentinfo/"


def get_data(id =None):
    data={}
    if id is not None:
        data={'id':id}
    data_pusing=json.dumps(data)
    sending_data=requests.get(url=URL,data=data_pusing)
    json_data=sending_data.json()
    print(json_data)

#get_data()

def post_data():
    data={
        'name' :'Sus',
        'roll' : 120,
        'city' : 'kolkata'
    }
    data_pursing=json.dumps(data)
    sending_data=requests.post(url=URL, data=data_pursing)
    json_data=sending_data.json()
    print(json_data)

post_data()

def update_data():
    data={
        'id': 1,
        'name' : 'Arijit',
        'city' : 'Tribeni'
    }

    persing_data=json.dumps(data)
    sending_data=requests.put(url=URL, data=persing_data)

    print(sending_data.json())

#update_data()

def delete_data():
    data={'id':3}
    persing_data=json.dumps(data)
    sending_data=requests.delete(url=URL, data=persing_data)
    print(sending_data.json())

#delete_data()