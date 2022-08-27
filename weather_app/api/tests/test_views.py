from django.test import Client, TestCase
from django.urls import reverse
from django.conf import settings


class GetWeatherForcastTest(TestCase):
    '''
        holds the blueprnt for tests 
    '''
    test_client = Client()

    def test_weather_api_request(self):
        '''
            Test to verify that api call returns success - 200
            test respnse has minimum, median, average and maximum
        '''
        
        url = "%s?days=%s"%(reverse('get-weather-data', args=["London"]), 2)
        response = self.test_client.get(url)
        print(response.json())
        json_response_data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('minimum', json_response_data)
        self.assertIn('maximum', json_response_data)
        self.assertIn('average', json_response_data)
        self.assertIn('median', json_response_data)
