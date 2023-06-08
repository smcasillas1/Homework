#Import necessary libraries to pull data from an API
import requests
import pandas as pd
import json
import os
from dotenv import load_dotenv

#load the API_Key environment
load_dotenv()

#get your API_key from the loaded environment above
api_key = os.getenv('API_KEY')


#Establishing an error handling task for my data pull request

try:
    #Initiate the data pull request from OpenWeatherMap API
    data_pull_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Orlando&appid='+api_key)

    #creating a conditional statement to validate the data pull
    if data_pull_request.status_code == 200:

        #Parsing the JSON data pull
        weather_data = json.loads(data_pull_request.text)
        print(weather_data)
    

    else:
        #Failed data pull request, error handling
        print(f"Your data pull request failure is due to {data_pull_request.status_code}")

except requests.exceptions.RequestException as re:
    print("Connection failed due to: ",re)



