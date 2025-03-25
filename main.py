# import requests
# city_name = 'New Delhi'
# API_key = 'c9740ee30283c1be3628338e6fcf334d'
#
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
#
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     print('Yes, We hit')
#     data = response.json()
#     print(data)

import requests

city_name = input("Enter the name of the city: ")
API_key = 'c9740ee30283c1be3628338e6fcf334d'  # Replace with your actual API key

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    print('Success:')
    data = response.json()
    print(data)
    # print("Weather is ", data['weather'])
    # print("Weather is ", data['weather'][0]) # call 0th index so it came out of list and become dictionary
    print("Weather is ", data['weather'][0]['description'])
    print("Current temperature is ", data['main']['temp'])
    print("Current temperature feels like is ", data['main']['feels_like'])
    print("Humidity is ", data['main']['humidity'])

elif response.status_code == 401:
    print('Invalid API key. Check if your key is correct or expired.')
elif response.status_code == 429:
    print('API rate limit exceeded. Try again later.')
else:
    print(f'Error {response.status_code}: {response.text}')
