# weather-api

Weather RESTful API that calculates the max, min, average and median temperature of a city from a public weather API

## SET UP

    - create a virtual environment for the project and activate it
    - install packages in the requirement doc via pip install -r requrements.txt
    - Have redis installed on your local machine. Redis is used as a cache store for the weather data from the open weather API
    - Have .env file with the following ENV variables
        DEBUG=True //debug setting (True or False)
        API_KEY=6aee9b026feb4e5ab4e132710212610 //weather api key
        SECRET_KEY=vzvcBsgZ1TW53-wWnIPZdqgk_ojmqLevE4kx1UtBpJo //generated project key, should be strong
        REDIS_URL=redis://127.0.0.1:6379 //redis server connection url

## RUN

    - Navigate to the project folder in terminal and run server --- python manage.py runserver

## TEST
    - Navigate to the following url on your browser or Postman changing city to any city around the world and your preferred number of days: 
    
    http://127.0.0.1:8000/api/locations/{city}/?days=2

## RUN UNIT TESTS
    - In the project folder in terminal run: python manage.py test![Screenshot from 2022-08-27 21-35-14](https://user-images.githubusercontent.com/8200075/187044136-3251acf0-486a-4774-83b4-14e84dca8e0e.png)
