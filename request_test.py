import requests

response = requests.get('https://openweathermap.org/api')

if response.status_code == 200:
       data = response.json()
       print(data)
else:
       print(f"Error: {response.status_code}")