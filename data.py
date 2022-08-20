import requests
import json


url = "https://opentdb.com/api.php"

parameters ={
    "amount" : 10,
    "type" : "boolean"
}

#get data from API
response = requests.get(url, params= parameters)
response.raise_for_status
#Store data from API in the variable data
question_data = response.json()['results']
