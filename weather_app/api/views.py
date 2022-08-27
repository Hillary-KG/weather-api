import json
import requests
import redis 
from statistics import median, mean

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from django.conf import settings
from django.core.cache import cache




# Create your views here.

@api_view(['GET'])
def get_weather_forcast(request, city=None):
    '''
        API view function to get temperature forcast for a city in a number of days 
        return: json-fromatted resposne with the min, max, average and median temperature
    '''

    try:
        if not city:
            return Response({
                'message': "Error! City not provided. Please provide a city to query"
            }, status=HTTP_400_BAD_REQUEST)

        days = request.GET.get('days')
        if not days:
            return Response({
                'message': "Error! No. of days not provided. Please provide days to query"
            }, status=HTTP_400_BAD_REQUEST)

        payload ={
            'key': settings.API_KEY,
            'q':  city,
            'days': days 
        }
        url = "http://api.weatherapi.com/v1/forecast.json"

        # query the cache first, if weather data not in cache then make request to api else use cached
        cached = cache.get(city)
        if not cached:


            api_response = requests.get(url, params=payload)
            json_response = api_response.json()

            forcast_days = json_response['forecast']['forecastday']
            mins = []
            maximums = []
            averages = []


            for day in forcast_days:
                # form a list of miminum temps
                mins.append(day['day']['mintemp_c'])
                # form a list of max temps
                maximums.append(day['day']['maxtemp_c'])
                # form a list of max temps
                averages.append(day['day']['avgtemp_c'])

            # compute the minimum by getting the average of the minimum temps
            minimum = mean(mins)

            # compute the maximum by getting the average of the maximum temps
            max = mean(maximums)
            
            # compute the average by getting the average of the average temps
            average = mean(averages)

            # compute the median by getting the median of the average temps
            median = mean(averages)

            resp = {
                'minimum': minimum,
                'maximum': max,
                'average': average,
                'median': median
            }
             # cache the results in redis for the next one hour
            cache.set(city, json.dumps(resp), 3600)
        else:
            # Loading from cache ....
            resp = json.loads(cached)
       

        return Response(resp, status=HTTP_200_OK)

    except Exception as e:
        # log exception here 
        print(f"An exception occured: {str(e)}")
        return Response({'Server Error'}, status=HTTP_500_INTERNAL_SERVER_ERROR)


