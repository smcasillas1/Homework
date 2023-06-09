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
    data_pull_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Memphis&appid='+api_key)

    #creating a conditional statement to validate the data pull
    if data_pull_request.status_code == 200:

        #Parsing the JSON data pull
        weather_data = json.loads(data_pull_request.text)
        
        #Picking the desired Weather location, Temperature and wind speeds
        weather_location = weather_data['name']
        weather_temp = weather_data['main']
        weather_winds = weather_data['wind']
        
        #Printing the weather details output for desired location
        print(f"City Chosen: {weather_location}, Current Temperature: {weather_temp['temp']}, Current Wind Speeds:{weather_winds['speed']} mph")
    

    else:
        #Failed data pull request, error handling
        print(f"Your data pull request failure is due to {data_pull_request.status_code}")

except requests.exceptions.RequestException as re:
    print("Connection failed due to: ",re)



